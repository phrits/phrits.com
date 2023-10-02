<?php
require('/home/cc55vfcn2kpt/public_html/init.php');
?>
<!DOCTYPE HTML>
<html>
	<head>
		<title>phrits.com &ndash; Credits</title>

<?php include $www . '/meta/head.html'; ?>

	</head>

	<body class="is-preload">
<?php include $www . '/meta/credits_header.html'; ?>

		<!-- Wrapper -->
		<div id="wrapper">
			<!-- Main -->
			<h1 class="major credits">Credits</h1>
			<h2 class="credits">Overview</h2>

			<div class="features" id="overview">
			<section style="width: auto;">
					<span class="icon solid major fa-code"></span>
					<p>
						The site design is based on <a href="https://html5up.net/hyperspace">Hyperspace &#124; @ajlkn</a> by <a href="https://html5up.net">HTML5 UP</a>, which I borrowed from heavily and then injected with a little bit of <a href="http://php.net">PHP</a> and other customizations for my own purposes. The design was made available free for personal and commercial use under the <a href="html5up.net/license">CCA 3.0 license</a>.
					</p>
				</section>
				<section>
				<span class="icon solid major fa-camera"></span>
					<p>
						With a few exceptions, all of the art and photography was done by someone else. Details can be found under <a href="#images">Images</a>, below.
					</p>
				</section>
				<section style="border: 0 !important;">
					<span class="icon solid major fa-book"></span>
					<p>
						Lots of my original content first appeared elsewhere: Now defunct websites, my old site(s), <a href="https://reddit.com/">Reddit</a> or <a href="https://facebook.com/">Facebook</a> posts and comments, etc. I've made a few minor additions, corrections, or updates here and there.
					</p>
				</section>
				<section style="width: auto; border: 0 !important;" id="wooden_board">
					<span class="icon solid major fa-solid fa-bread-slice"></span>
					<p>
						The wooden board at the bottom of the page represents my personal philosphy of openness and honesty. It also symbolizes my belief that food should be better than mere sustenance. Everything should be &quot;above board&quot;.
					</p>
				</section>    
			</div>

		<?php include 'image_credits.html'; ?>

		<h2 class="credits" id="old_phrits">2011 version of <span class="phrits-invert">phrits.com</span></h2>
		<div class="features">
			<section style="width: auto;">
				<span class="icon solid major"><img src="/images/phrits-favicon.ico" alt="p" /></span>
					<p>
						At launch in February, 2023, almost all original content came from the old site. Recipes, writing, etc.
					</p>
					<p>
						I've had a few false starts trying to relaunch. The version I put up over a decade ago was a home grown content management system written in PHP. Except that I didn't code a front end. Adding new content was obnoxious.
					</p>
					<p>
						When I started my March 2022 attempt, I copied everything over to a separate subdomain and tweaked it until it worked. Alas, the site was implemented in PHP v5.6&mdash;current when it was developed&mdash;and PHP is up to v8.1 now. The old site is there, but program execution fails. The effort involved in updating that code just isn't worth the result. Please <a href="mailto:missingOld@phrits.com">let me know</a> if you're missing something.
					</p>
			</section>
		</div> <!-- class="features" -->



		</div> <!-- wrapper -->

<?php include $www . '/meta/footer.html'; ?>
<?php include $www . '/meta/scripts.html'; ?>

	</body>
</html>
