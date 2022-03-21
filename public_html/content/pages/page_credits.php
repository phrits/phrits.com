<?php
require("/home/xxxredactedxxx/public_html/cgi-bin/init.php");

doctype();
?>

<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
<?php
    include($www . "/content/parts/part_head.php");
    description("Source material for some content and images");
    html_meta(array("keywords"      => 'contributors'));
    html_simple("title", "Credits and Attributions - phrits.com")->output();

    html_simple("title", "");
?>
    </head>
    <body>
        <div id="above_board"> <!-- Everything but the sticky footer. -->

<?php
include($www . "/content/parts/part_banner.php");
?>
            <div class="outerband">
<?php
include($www . "/content/parts/part_image_credits.php");
include($www . "/content/parts/part_document_credits.php");
?>
            </div> <!-- class="outerband" -->
<?php
include($www . "/content/parts/part_footer.php");
include($www . "/content/parts/part_board.php");
?>
    </body>
</html>
