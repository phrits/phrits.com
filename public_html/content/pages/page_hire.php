<?php
require("/home/brobip/public_html/cgi-bin/init.php");

doctype();
?>

<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
<?php
    include($www . "/content/parts/part_head.php");
    description("Fritz Knack's employment status and availability for interesting challenges. Seeking job in a Test Kitchen");
    html_meta(array("keywords"      => "Food Geek"));
    html_meta(array("keywords"      => "Food, Cooking, Cook, resume"));
    html_meta(array("keywords"      => "Food Science, writer, blog, mise en place"));
    html_meta(array("keywords"      => "data analysis, excel, sql, database"));
    html_meta(array("keywords"      => "analysis, technical writer, perl, python"));
    html_meta(array("keywords"      => "sharepoint, word, ms-word, access, powerpoint, office"));
    html_simple("title", "Hire Me! - phrits.com")->output();
?>
    </head>
    <body>

       <div id="above_board"> <!-- Everything but the sticky footer. -->
<?php
    include($www . "/content/parts/part_banner.php");
    include($www . "/content/parts/part_hire.php");
    include($www . "/content/parts/part_footer.php");
    include($www . "/content/parts/part_board.php");
?>
    </body>
</html>
