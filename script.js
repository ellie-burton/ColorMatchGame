let red, green, blue;
let redOutput, greenOutput, blueOutput;
let guessR, guessG, guessB;
let run = true;

function setup() {
  let canvas = createCanvas(1000, 600);
  canvas.parent('gameCanvas');

  red = createSlider(0, 255, 0);
  red.position(100, 100);

  green = createSlider(0, 255, 0);
  green.position(100, 300);

  blue = createSlider(0, 255, 0);
  blue.position(100, 500);

  redOutput = createInput('');
  redOutput.position(550, 100);
  redOutput.size(50, 50);
  redOutput.attribute('readonly', '');

  greenOutput = createInput('');
  greenOutput.position(550, 300);
  greenOutput.size(50, 50);
  greenOutput.attribute('readonly', '');

  blueOutput = createInput('');
  blueOutput.position(550, 500);
  blueOutput.size(50, 50);
  blueOutput.attribute('readonly', '');

  guessR = Math.floor(random(0, 256));
  guessG = Math.floor(random(0, 256));
  guessB = Math.floor(random(0, 256));
}

function draw() {
  background(255);

  noStroke();
  fill(guessR, guessG, guessB);
  rect(700, 200, 100, 100);

  let redVal = red.value();
  let greenVal = green.value();
  let blueVal = blue.value();

  redOutput.value(redVal);
  greenOutput.value(greenVal);
  blueOutput.value(blueVal);

  fill(redVal, greenVal, blueVal);
  rect(700, 400, 100, 100);
}

function drawCheckScreen() {
  let diff = 100 - ((Math.abs(guessR - red.value()) / 255) / 3 + (Math.abs(guessG - green.value()) / 255) / 3 + (Math.abs(guessB - blue.value()) / 255) / 3) * 100;
  let output = createInput('');
  output.position(700, 100);
  output.size(150, 50);
  output.value(round(diff, 2) + "%");
}

function keyPressed() {
  if (keyCode === 32) {
    drawCheckScreen();
  }
}

function windowResized() {
  resizeCanvas(1000, 600);
}
