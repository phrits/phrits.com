<?php
require('/home/brobip/subdomtest.phrits.com/init.php');
?>
<!DOCTYPE HTML>
<html>
	<head>
        <title>Recipe Title - phrits.com</title>
        <meta name="description" content="" />
<?php include $www . '/meta/head.html'; ?>
    </head>
	<body class="is-preload">
		<!-- Header -->
        <?php include $www . '/recipes/recipes_header.html'; ?>
        <div class="wrapper style3 recipe">
            <h1>Crazy Cake</h1>
            <p>This recipe is based on &quot;Crazy Mixed-up Chocolate Cake&quot; from <i>A Piece of Cake</i> by Susan G. Purdy, 1989.</p>
            <h2>Ingredients</h2>
            <ul>
                <li class="ingredient">3 cups unbleached, all-purpose flour</li>
                <li class="ingredient">1/2 cup unsweetened cocoa, Herhey's Special Dark (Dutch processed) preferred</li>
                <li class="ingredient">1 teaspoon salt</li>
                <li class="ingredient">2 cups sugar</li>
                <li class="ingredient">2 teaspoons baking soda</li>
                <li class="ingredient">2 tablespoons white or cider vinegar</li>
                <li class="ingredient">2 teaspoons vanilla extract</li>
                <li class="ingredient">2/3 cup vegetable oil</li>
                <li class="ingredient">2 cups lukewarm water</li>
            </ul>
            <h2>Instructions</h2>
            <ol>
                <li>Heat oven to 350&deg;F/175&deg;C.
                <li>(Optional) Sift the dry ingredients together.</li>
                <li>Combine all ingredients in a bowl. You can just use the baking pan if you prefer.</li>
                <li>Pour into an ungreased 9x13 baking pan.</li>
                <li>Bake for 30-35 minutes or until a toothpick comes out clean.</li>
                <li>Allow to cool slightly before serving. Serve plain or dressed up as desired.</li>
            </ol>
            <h2>Yield</h2>
            <p>Serves about 12.</p>
        </div> <!-- "wrapper style3 recipe" -->

<?php include '../../footer.html'; ?>
<?php include '../../scripts.html'; ?>

        </body>
</html>
