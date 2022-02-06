<?php
include_once "header.php";
require_once 'vendor/autoload.php';
putenv('GOOGLE_APPLICATION_CREDENTIALS=visionAPIkey.json');

use Google\Cloud\Vision\V1\ImageAnnotatorClient;

if ($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['analyseImg'])) {
    analyseImage();
}
function analyseImage()
{
    echo 'Analysing...';
    try {
        $imageAnnotatorClient = new ImageAnnotatorClient();

        $image_path = 'https://i3.ytimg.com/vi/oeVPsNBTWqU/hqdefault.jpg';
        $imageContent = file_get_contents($image_path);
        $response = $imageAnnotatorClient->textDetection($imageContent);
        $text = $response->getTextAnnotations();
        echo $text[0]->getDescription();

        if ($error = $response->getError()) {
            print('API Error: ' . $error->getMessage() . PHP_EOL);
        }

        $imageAnnotatorClient->close();
    } catch (Exception $e) {
        echo $e->getMessage();
    }
}
?>

<script language="JavaScript" type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<script language="JavaScript" type="text/javascript" src="https://cdn.jsdelivr.net/npm/@google-cloud/vision@2.4.2/build/src/index.min.js"></script>
<script>
    windowHeight = $(window).height() * 0.5;
    windowWidth = $(window).width() * 0.8;
</script>

<div>
    <video id="videoOCR" playsinline autoplay></video>
</div>

<div style="text-align: center;">
    <button id="takePicture">Capture</button>
</div>
<!-- 
<form action="consumptionHabits.php" method="post">
    <input type="submit" name="analyseImg" value="GO" />
</form> -->

<canvas id="canvasOCR" style="background-color: gray;">
</canvas>
<!-- <button>Toggle Camera</button> -->
<p style="text-align: center;">Please take an image for analysis.</p>
<script>
    const canvas = document.getElementById('canvasOCR');
    canvas.width = windowWidth;
    canvas.height = windowHeight;
    `use strict`;

    const video = document.getElementById('videoOCR')

    const constraints = {
        audio: false,
        video: {
            width: windowWidth, //ideal: //gets max resolution
            height: windowHeight
        }
    };

    async function init() {
        try {
            const stream = await navigator.mediaDevices.getUserMedia(constraints);
            handleSuccess(stream);
        } catch (e) {

        }
    }

    function handleSuccess(stream) {
        window.stream = stream;
        video.srcObject = stream;
    }

    init();

    var context = canvas.getContext('2d');
    takePicture.addEventListener("click", function() {
        context.drawImage(video, 0, 0, windowWidth, windowHeight)
        imgData = canvas.toDataURL("image/png")
        localStorage.setItem("imgData", imgData);
    })
</script>

<?php
include_once "footer.php";
?>