# WorkLog

## 2022-03/18

![](meta_images/20220319-proto_schreenshot.jpg)

It's ugly, but it's a start.

## 2022-03-17/18

Finally got the last Archive Disclaimer banner working. Geez, I had hard calls to the old init.php for days!

Got git set up with cPanel. Lots easier with a public repo. Above board indeed.

Decided against worrying about getting virtualenv set up on the linux side of things, at least for now. Deleted what I could find of that and other remnants including the django folder, virtualenv folder. I'll end up reinstalling fresh if I need it later anyway, so the remaining bin files sticking around aren't hurting anything.

Added a LICENSE to the repo. CC 1.0 Universal, or something similar.

I had yet another hard drive crash, and the usual flailing about with Dropbox fucked up my installed programs. Thus:

### Fresh

- Python (3.10.10)

- Anaconda (4.10.3. Giant installation.)

- PostgreSQL

- pgAdmin

- Flask

- Django

- Jupyter

- pandas

- SQLAlchemy

See [`2022-03-18.requirements.txt`](2022-03-18.requirements.txt) for specifics.

### Not Updated

#### VS Code
```
Version: 1.65.2 (user setup)
Commit: c722ca6c7eed3d7987c0d5c3df5c45f6b15e77d1
Date: 2022-03-10T14:33:55.248Z
Electron: 13.5.2
Chromium: 91.0.4472.164
Node.js: 14.16.0
V8: 9.1.269.39-electron.0
OS: Windows_NT x64 10.0.22000
```

- gitbash (2.34.1.windows.1)

## 2022-03-05

Repo setup. `$www . "/content/parts/part_splash.php"` reflecting same.

### Visual Notes

#### Comfortable Colors

[Source](https://www.nexcess.net/blog/web-design-trends/)

Consider for the palate making the main, the dark blue brigher by 20% or so. Highlight yellow gets muted or morphed appropriately.

##### Potential blue: #0000AA

[Neumorphism.io](https://neumorphism.io/#0000AA)

```
border-radius: 32px;
background: linear-gradient(145deg, #0000fa, #0000d3);
box-shadow:  16px 16px 32px #000075,
             -16px -16px 32px #0000ff;
```

##### Maroon: #663333

[neumorphic.design](https://neumorphic.design/)

```
background: linear-gradient(145deg, #783C3C, #542A2A);
border-radius: 15%;
box-shadow: 7.21px 7.21px 9px #3F1F1F, -7.21px -7.21px 9px #8D4747;
```
Consider dark mode backgrounds to make stuff jump when it should.

#### Neumorphism

Looks self-codable, but there appear to be some free wheels out there already. Generators such as [Neumorphism.io](https://neumorphic.design/) include concavity and inset for input parameters, then produce borders and shadows. Examples:

```
background: linear-gradient(145deg, #6677DB, #465397);
border-radius: 36%;
box-shadow: 7.21px 7.21px 9px #353E72, -7.21px -7.21px 9px #778CFF;
```

```
border-radius: 50px;
background: linear-gradient(145deg, #0000f5, #0000ce);
box-shadow:  25px 25px 35px #000073,
             -25px -25px 35px #0000ff;
```


Pictures. Graphics.