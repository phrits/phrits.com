<?php
require("/home/brobip/public_html/cgi-bin/init.php");

doctype();
?>

<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
<?php
    include($www . "/content/parts/part_head.php");
    html_meta(array("keywords"      => 'Chili, Tex-Mex, Chili Powder, Mexican'));
    html_meta(array("keywords"      => 'chile, chiles, pasilla, guajillo'));
    html_meta(array("keywords"      => 'chiles de arbol, ancho'));
    html_simple("title", "Chili Powder - phrits.com")->output();
?>
    </head>
    <body>

       <div id="above_board"> <!-- Everything but the sticky footer. -->
<?php
    include($www . "/content/parts/part_banner.php");
    include($www . "/content/parts/part_chili_powder.php");
    include($www . "/content/parts/part_footer.php");
    include($www . "/content/parts/part_board.php");
?>
    </body>
</html>
