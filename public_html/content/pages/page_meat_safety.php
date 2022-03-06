<?php
require("/home/brobip/public_html/cgi-bin/init.php");

doctype();
?>

<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
<?php
    include($www . "/content/parts/part_head.php");
    description("What should I know about meat and food safety?");
    html_meta(array("keywords"      => "Food Geek"));
    html_meta(array("keywords"      => "raw meat, safety, e. coli, salmonella, trichonosis"));
    html_meta(array("keywords"      => "meat, poultry, beef, pork"));
    html_simple("title", "Easy to Understand Meat Safety - phrits.com")->output();
?>
    </head>
    <body>

       <div id="above_board"> <!-- Everything but the sticky footer. -->
<?php
    include($www . "/content/parts/part_banner.php");
    include($www . "/content/parts/part_meat_safety.php");
    include($www . "/content/parts/part_footer.php");
    include($www . "/content/parts/part_board.php");
?>
    </body>
</html>
