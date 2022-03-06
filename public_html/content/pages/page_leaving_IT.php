<?php
require("/home/brobip/public_html/cgi-bin/init.php");

doctype();
?>

<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
<?php
    include($www . "/content/parts/part_head.php");
    description("Walking away from a 25-year career is a big step.");
    html_meta(array("keywords"      => 'Information Technology, Technical Business Analyst'));
    html_meta(array("keywords"      => 'Business Process, Process Modeling, Process Development, Process Improvement'));
    html_meta(array("keywords"      => "Food Geek"));
    html_simple("title", "Why I'm Leaving IT - phrits.com")->output();
?>
    </head>
    <body>

       <div id="above_board"> <!-- Everything but the sticky footer. -->
<?php
    include($www . "/content/parts/part_banner.php");
    include($www . "/content/parts/part_leaving_IT.php");
    include($www . "/content/parts/part_footer.php");
    include($www . "/content/parts/part_board.php");
?>
    </body>
</html>
