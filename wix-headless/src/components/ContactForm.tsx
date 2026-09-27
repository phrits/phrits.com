import { useState } from "react";
import { submissions } from "@wix/forms";

interface FormField {
  label: string;
  target: string;
  required: boolean;
  componentType: string;
  identifier?: string;
  options?: { value: string; label: string }[];
}

interface ContactFormProps {
  formId: string;
  fields: FormField[];
}

export default function ContactForm({ formId, fields }: ContactFormProps) {
  const [formData, setFormData] = useState<Record<string, string>>({});
  const [status, setStatus] = useState<"idle" | "submitting" | "success" | "error">("idle");
  const [fieldErrors, setFieldErrors] = useState<Record<string, string>>({});

  const updateField = (target: string, value: string) => {
    setFormData((previous) => ({ ...previous, [target]: value }));
    if (fieldErrors[target]) {
      setFieldErrors((previous) => {
        const next = { ...previous };
        delete next[target];
        return next;
      });
    }
  };

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setStatus("submitting");
    setFieldErrors({});

    try {
      const result = await submissions.createSubmission({ formId, submissions: formData });

      if (result.status === "PENDING" || result.status === "CONFIRMED") {
        setStatus("success");
        setFormData({});
        return;
      }

      setStatus("error");
    } catch (error: unknown) {
      const violations =
        (error as { details?: { validationError?: { fieldViolations?: unknown[] } } })
          ?.details?.validationError?.fieldViolations ?? [];
      const nextErrors: Record<string, string> = {};

      for (const violation of violations as Array<{
        data?: { errors?: Array<{ errorPath?: string; errorMessage?: string }> };
      }>) {
        for (const fieldError of violation.data?.errors ?? []) {
          if (fieldError.errorPath && !nextErrors[fieldError.errorPath]) {
            nextErrors[fieldError.errorPath] = fieldError.errorMessage ?? "Please check this field.";
          }
        }
      }

      if (Object.keys(nextErrors).length) {
        setFieldErrors(nextErrors);
        setStatus("idle");
      } else {
        setStatus("error");
      }
    }
  };

  if (status === "success") {
    return (
      <div className="form-success" role="status" tabIndex={-1}>
        <strong>Thank you.</strong> Your note is on its way to Fritz.
      </div>
    );
  }

  return (
    <form onSubmit={handleSubmit} className="form-container">
      {fields.map((field) => {
        const inputId = `contact-${field.target}`;
        const errorId = `${inputId}-error`;
        const hasError = Boolean(fieldErrors[field.target]);
        const commonProps = {
          id: inputId,
          name: field.target,
          required: field.required,
          value: formData[field.target] ?? "",
          "aria-invalid": hasError,
          "aria-describedby": hasError ? errorId : undefined,
          onChange: (event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) =>
            updateField(field.target, event.target.value),
        };

        return (
          <div key={field.target} className="form-field">
            <label className="form-label" htmlFor={inputId}>
              {field.label || field.target.replaceAll("_", " ")}
              {field.required && <span className="required" aria-hidden="true"> *</span>}
            </label>

            {field.componentType === "DROPDOWN" && field.options ? (
              <select {...commonProps} className={`form-select${hasError ? " form-input-error" : ""}`}>
                <option value="">Select an option</option>
                {field.options.map((option) => (
                  <option key={option.value} value={option.value}>{option.label}</option>
                ))}
              </select>
            ) : field.identifier === "TEXT_AREA" || field.target === "message" ? (
              <textarea {...commonProps} rows={6} className={`form-textarea${hasError ? " form-input-error" : ""}`} />
            ) : (
              <input
                {...commonProps}
                type={field.target === "email" ? "email" : field.componentType === "PHONE_INPUT" ? "tel" : "text"}
                autoComplete={
                  field.target === "email" ? "email" :
                  field.target === "first_name" ? "given-name" :
                  field.target === "last_name" ? "family-name" :
                  field.target === "phone" ? "tel" : undefined
                }
                className={`form-input${hasError ? " form-input-error" : ""}`}
              />
            )}

            {hasError && <p id={errorId} className="form-field-error">{fieldErrors[field.target]}</p>}
          </div>
        );
      })}

      <button type="submit" disabled={status === "submitting"} className="form-button">
        {status === "submitting" ? "Sending…" : "Send message"}
      </button>

      {status === "error" && (
        <p className="form-error" role="alert">Something went wrong. Please try again.</p>
      )}
    </form>
  );
}
