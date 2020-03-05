<?php

?>
<html>
    <body>
        <script>
            function checkForThreeRadioBtns() {
						if ($('input[name=1]').is(':checked') && 
							$('input[name=2]').is(':checked') && 
							$('input[name=3]').is(':checked')) {
								 turnSubmitBlue();
						}
					 }
        </script>
    </body>
</html>
