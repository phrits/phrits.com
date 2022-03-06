<?php
/*******************************************************************************
*
*   filename:                   phrits.css.php
*   site:                       phrits.com
*   author:                     Fritz Knack
*   date:                       2011-12-27 11:54
*
/******************************************************************************/
header("Content-type: text/css");

include('../css/colors.php');
// include('../css/mobile.css.php');

?>

* {
    margin:                 0;
    padding:                0;
    max-width:              100%; /* Keeps pictures, etc. within their boxes. */
}

html,
body {
    background:             <?php echo $color_background; ?>;
/*    height:                 100%; */ /* Disabling causes it to *not* stick to bottom of viewport. */
}
body {
    font-family:            <?php echo $font_sans; ?>;
    color:                  <?php echo $color_primary; ?>;
}
div {
}
p {
    padding:                1ex 1ex 1ex 0;
}
ul, ol {
    list-style-position:    inside;
    padding-bottom:         0;
    padding-top:            0;
    margin-bottom:          1em;
}
li {
    padding:                0 0 0 0;
    margin-bottom:          1ex;
}
ul li {
    margin-left:            1em;
}
img {
    border:                 0;
}
a {
}
a:link {
    color:                  <?php echo $color_secondary ?>;
}

a:visited {
    color:                  <?php echo $color_gray ?>;
}
a:active {
    color:                  <?php echo $color_accent ?>;
    background:             <?php echo $color_secondary; ?>;
}
a:hover {
    color:                  <?php echo $color_accent ?>;
    background:             <?php echo $color_secondary; ?>;
}

a:hover img,
img a:hover {
    border:                 0 0 0 0;
    text-decoration:        none;
}

h1, h2, h3,
h4, h5, h6 {
    font-family:            <?php echo $font_sans; ?>;
    color:                  <?php echo $color_secondary ?>;
}
h1 {
    font-size:              1.5em;
}
h2 {
    font-size:              1.2em;
}
h3 {
    font-size:              1em;
}
blockquote {
    margin:                 1em 8% 1em 8%;
    padding:                1em 2% 1em 2%;;
    border:                 6px solid <?php echo $color_secondary ?>;
    border-top:             0;
    border-bottom:          0;
    border-radius:          3em;

}
blockquote:first-letter {
    font-size:              200%;
    font-weight:            bold;
    color:                  <?php echo $color_secondary ?>;
}

dt {
    font-size:              120%;
    font-weight:            bold;
    color:                  <?php echo $color_secondary ?>;
}


.caption {
    font-size:              70%;
    font-family:            sans-serif;
}
.code {
    font-family:            <?php echo $font_mono; ?>;
}
.highlight,
.emph {
    color:                  <?php echo $color_secondary ?>;
    font-weight:            bold;
}

.exposition:first-line {
    font-weight:            bold;
}

.foreign {
    font-style:             italic;
}
.title {
    font-style:             italic;
    font-variant:           small-caps;
}
.dietary {
    font-variant:           small-caps;
    font-weight:            bold;
}
.nobullet,
.ingredient,
.credits {
    list-style:             none;
    margin-left: 0;
}

.credits li {
    margin-bottom: 1em;
}
.oneline li {
    display:                inline-block;
    padding:                0 1ex 0 0;
}
.left {
    text-align:             left;
}
.right {
    text-align:             right;
}
.center {
    text-align:             center;
}


aside {
    max-width:              33%;
    min-width:              25%;
    border:                 3px ridge;
    padding:                1ex;
    text-align:             left;
}
aside.r {
    float:                  right;
    margin-left:            1ex;
}
aside.l {
    float:                  left;
    margin-right:           1ex;
}

.inline {
    display:                inline;
}

/* Page */
#above_board        {
    min-height:             100%;
    margin: 0 auto;
}
#board          {
    height:                 32px;
    width:                  100%;
    margin-top:             -32px;  /* negative margin-top equals height of #board */
    background:             url("/images/board.png");
    /* board image: http://farm4.static.flickr.com/3254/2779025080_c38653e1a5.jpg */
}

/* Banner */
#banner {
    background:             <?php echo $color_primary ?>;
    position:               fixed;
    width:                  100%;
}
#banner .colorband {
    padding-bottom:         1px; /* There's an extra px floating around somewhere above. */
    background:             url("/images/underbanner.png");
    height:                 16px;
}
#banner img {
    background:             <?php echo $color_primary ?>; /* Hides link hover ugliness. */
    border:                 0;
    padding:                1em 0 1em 1em;
}
#content_pad {
    margin:                 0;
    padding:                117px 0 0 0;    /* underbanner image plus logo image plus #top_menu heights */
}

/* Footer */
#footer {
clear:both;
    background:             <?php echo $background_images; ?>;
    background-position:    12%, top left;
    background-size:        auto, 12% auto;
    background-repeat:      repeat-y;
    margin:                 0 10% 32px 0; /* 32px is height of #board */
    font-size:              80%;
    text-align:             right;
}

#footer p {
    font-size:              85%;
    margin-left:            30%;
}

/* Content */
.outerband,
.splash {
    background:             <?php echo $background_images; ?>;
    background-position:    12%, top left;
    background-size:        auto, 12% auto;
    background-repeat:      repeat-y;
    padding:                2em 2em 0 2em;
}

.outerband {
    margin:                 0 10% 0 0;
}

.splash {
/*    display: none; */
    margin:                 0 10% 0 0;
    color:                  <?php echo $color_splash; ?>
}

.splash h1,
.splash h2,
.splash h3,
.splash h4,
.splash h5,
.splash h6 {
    color:                  <?php echo $color_primary; ?>
}

.splash .innerband {
    border:                 4px double <?php echo $color_splash; ?>;
    border-right:           0;
    font-size:              80%;
    margin-left:            10%;
    box-shadow:             0px -4px 10px 0 <?php echo $color_splash ?>;
}


#top_menu {
    background:             <?php echo $background_images; ?>;
    background-position:    12%, top left;
    background-size:        auto, 12% auto;
    background-repeat:      repeat-y;
    font-family:            <?php echo $font_sans; ?>;
    color:                  <?php echo $color_white; ?>;
    margin:                 0 10% 0 0;
    padding:                0 2em 0 2em;
}

#top_menu * {
    text-align: right;
    color:                  <?php echo $color_white; ?>;
}

#top_menu li {
    margin-bottom:          0; /* Overrides global li bottom margin of 1ex */
}


#top_menu a:hover {
    color:                  <?php echo $color_accent ?>;
    background:             <?php echo $color_secondary; ?>;
}

#top_menu li {
    padding:                0 1ex 0 1ex;
}

#top_menu ol,
#top_menu ul {
    margin-bottom:          0;
}

.innerband {
    margin:                 0;
    border:                 3px solid <?php echo $color_primary ?>;
    border-right:           0;
    background:             <?php echo $color_background; ?>;
    border-radius:          1em 0 0 1em;
    padding:                1em;
height: auto !important;
}

.insetRight,
.insetRight_small {
    float:                  right;
    border:                 3px solid <?php echo $color_secondary ?>;
    padding:                1ex;
    border-radius:          0 0em 0 1em;
    border-top:             0;
    border-right:           0;
    margin:                 1em 0 1ex 1ex;
    text-align:             right;
    box-shadow:             0 -5px 12px 0px <?php echo $color_primary ?>;
    max-width:              33%;
}

.insetRight_small p {
    font-size:              80%;
    }

.insetLeft {
    float:                  left;
    border:                 3px solid <?php echo $color_secondary ?>;
    padding:                1ex;
    border-radius:          0 0em 1em 0em;
    border-top:             0;
    border-left:            0;
    margin:                 1em 1ex 1ex 0;
    text-align:             left;
    box-shadow:             0 -5px 10px 0px <?php echo $color_primary ?>;
    max-width:              33%;
}

.insetRight_cpowder,
.insetLeft_cpowder {
    max-width:              100%;
}

.spaced {
    padding-left:           5px;
    padding-right:          5px;
}

.phrits,
a.phrits,
a:link.phrits,
a:visited.phrits,
a:active.phrits {
    font-family:            <?php echo $font_mono; ?> !important;
    font-size:              105%;
    font-weight:            bold;
    color:                  <?php echo $color_black ?> !important;
    text-decoration:        none !important;
    border:                 0 0 0 0 !important;
}
a:hover.phrits {
    color:                  <?php echo $color_accent ?>;
    background:             <?php echo $color_secondary; ?>;
}

.noscreen {
    display: none !important;
}

.photo_step {   /* Used in the Chili Powder photo essay. */
    clear:                  both;
    border-top:             1px dotted <?php echo $color_primary; ?>;
    max-width:              85%;
}

@media print {
    html,
    body {
        font-family:            <?php echo $font_serif; ?>;
        background:             <?php echo $color_white; ?>;
        color:                  <?php echo $color_black; ?>;
    }

    a {
        text-decoration: none !important;
    }

    .noprint {
        display: none !important;
    }

    #top_menu,
    #board,
    .colorband {
        display: none !important;
    }
    #content_pad {
        padding-top:            0;  /* Reset #board adjustment. */
    }

    #footer {
        margin-bottom:          0;  /* Reset #board adjustment. */
    }

}

/*
            header {
                clear: both;
                margin-left: auto;
                margin-right: auto;
            }
            header > h1 {
                text-align: center;
            }
            b {
                font-weight: 501; /* Normal = 400; Bold = 700. IE11 lacks that subtlety; 501 = Bold */
                color: #660000;
            }
*/