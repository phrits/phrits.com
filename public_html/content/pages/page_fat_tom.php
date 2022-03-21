<?php
require("/home/xxxredactedxxx/public_html/cgi-bin/init.php");

doctype();
?>

<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
<?php
    include($www . "/content/parts/part_head.php");
    description("Know your food safety: Food, Acidity, Time, Temperature, Oxygen, Moisture");
    html_meta(array("keywords"      => "Food Geek"));
    html_meta(array("keywords"      => 'FAT TOM, ServSafe, HACCP, food safety, biological hazard'));
    html_simple("title", "FAT TOM - phrits.com")->output();
?>
    </head>
    <body>

       <div id="above_board"> <!-- Everything but the sticky footer. -->
<?php
    include($www . "/content/parts/part_banner.php");
    include($www . "/content/parts/part_fat_tom.php");
    include($www . "/content/parts/part_footer.php");
    include($www . "/content/parts/part_board.php");
?>
    </body>
</html>
