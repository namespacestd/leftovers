var currentSlide = 1;
var slideNumber = 0;

var currentNews = 1;

function startSlideshow(numSlides){
	try{
		hideAll(numSlides);
		slideNumber = numSlides;
		setInterval(function(){slideShow()}, 6000);
	}
	catch(err){
	}
}

function hideAll(numSlides){
	for(var i=2; i<=numSlides;i++){
		$("#slide"+i).css("display", "none");
	}
}

function slideShow(){
	$('#slide'+currentSlide).fadeOut(2000);
	currentSlide = currentSlide + 1;
	if(currentSlide > slideNumber)
		currentSlide = 1;
	$('#slide'+currentSlide).fadeIn(2000);
}