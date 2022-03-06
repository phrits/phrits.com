<?
/*******************************************************************************
*
*   filename:                   mobile.css.php
*   site:                       phrits.com
*   author:                     Fritz Knack
*   date:                       2013-01-15 15:00:53
*
* NOT USED (2016-05-25, just stopping by.)
******************************************
*
/******************************************************************************/
header("Content-type: text/css");

include('../css/colors.php');

?>
* {
    float: none !important;
    font-size: 12px;
    text-align: left;
}

div {
    clear: both !important;
}


h1, h1, h3,
h4, h5, h6 {
	font-weight: normal;
}

img {
	max-width: 250px;
	display: block;
}

.center {
	width: 100% !important;
	text-align: center;
}

.right {
    text-align: left;
}

.insetRight,
.insetRight_small,
.insetRight {
    border:                 3px solid <?php echo $color_secondary ?>;
    padding:                1ex;
    border-radius:          0 0em 1em 1em;
    margin:                 1ex;
    box-shadow:             0 -5px 10px 0px <?php echo $color_primary ?>;
    max-width:              90%;
}
