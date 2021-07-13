// ================ХЕДЕР================================
var newWidth = window.innerWidth;
window.onresize = function () {
	newWidth = window.innerWidth;
	//Подменю
	$('#abiturient').removeClass("active");
	$('.abiturient-menu').removeClass("active");
	$('#abiturient').removeClass("_active");
	$('.abiturient-menu').removeClass("_active");
	$("#college").removeClass("active");
	$(".college-menu").removeClass("active");
	$("#give-docs").removeClass("active");
	$(".give-docs-menu").removeClass("active");
	///Подподменю
	$("#college").removeClass("_active");
	$(".college-menu").removeClass("_active");
	$("#spec").removeClass("active");
	$(".spec-menu").removeClass("active");
	$("#spec").removeClass("_active");
	$(".spec-menu").removeClass("_active");
	// if($('.abiturient-menu-responsive').hasClass('done')){
	// 	$('.abiturient-menu-link').appendTo($('.abiturient-menu'));
	// 	$('.abiturient-menu-responsive').removeClass('done')
	// }	
}

//Подменю абитуринта
$('#abiturient').mouseover(function(){
	if (newWidth> 767.98){
		$('#abiturient').addClass("active");
		$('.abiturient-menu').addClass("active");
	}
}).mouseout(function(){
	if (newWidth> 767.98){
		$('#abiturient').removeClass("active");
		$('.abiturient-menu').removeClass("active");
	}
});
$('.abiturient-menu').mouseover(function(){
	if (newWidth> 767.98){
		$('#abiturient').addClass("active");
		$('.abiturient-menu').addClass("active");
	}
}).mouseout(function(){
	if (newWidth> 767.98){
		$('#abiturient').removeClass("active");
		$('.abiturient-menu').removeClass("active");
	}
});

//Подменю колледжа
$("#college").mouseover(function(){
	if (newWidth> 767.98){
		$("#college").addClass("active");
		$(".college-menu").addClass("active");
	}
}).mouseout(function(){
	if (newWidth> 767.98){
		$("#college").removeClass("active");
		$(".college-menu").removeClass("active");
	}
});
$(".college-menu").mouseover(function(){
	if (newWidth> 767.98){
		$("#college").addClass("active");
		$(".college-menu").addClass("active");
	}
}).mouseout(function(){
	if (newWidth> 767.98){
		$("#college").removeClass("active");
		$(".college-menu").removeClass("active");
	}
});

// Подменю подачи документов
$("#give-docs").mouseover(function(){
	if (newWidth> 767.98){
		$("#give-docs").addClass("active");
		$(".give-docs-menu").addClass("active");
	}
}).mouseout(function(){
	if (newWidth> 767.98){
		$("#give-docs").removeClass("active");
		$(".give-docs-menu").removeClass("active");
	}
});
$(".give-docs-menu").mouseover(function(){
	if (newWidth> 767.98){
		$("#give-docs").addClass("active");
		$(".give-docs-menu").addClass("active");
	}
}).mouseout(function(){
	if (newWidth> 767.98){
		$("#give-docs").removeClass("active");
		$(".give-docs-menu").removeClass("active");
	}
});
//Подподменю в колледже для специальности
$("#spec").mouseover(function(){
	if (newWidth> 767.98){
		$("#spec").addClass("active");
		$(".spec-menu").addClass("active");
	}
}).mouseout(function(){
	if (newWidth> 767.98){
		$("#spec").removeClass("active");
		$(".spec-menu").removeClass("active");
	}
});
$(".spec-menu").mouseover(function(){
	if (newWidth> 767.98){
		$("#spec").addClass("active");
		$(".spec-menu").addClass("active");
		$("#college").addClass("active");
		$(".college-menu").addClass("active");
	}
}).mouseout(function(){
	if (newWidth> 767.98){
		$("#spec").removeClass("active");
		$(".spec-menu").removeClass("active");
		$("#college").removeClass("active");
		$(".college-menu").removeClass("active");
	}
});
// Главное меню
let iconMenu = document.querySelector(".icon-menu");
if (typeof body === 'undefined') {
    const body = document.querySelector('body');
}

let navigation = document.querySelector(".navigation");
if (iconMenu) {
	iconMenu.addEventListener("click", function () {
		iconMenu.classList.toggle("active");
		body.classList.toggle("lock");
		navigation.classList.toggle("active");
	});
}

//Adaptive functions
$(window).resize(function(event) {
	adaptive_function();
});

//Подменю для телефонного разрешения
function adaptive_header(w,h) {
		var nav=$('.navigation');
		var aMR=$('.abiturient-menu-responsive');
		var aML=$('.abiturient-menu-link');
		var aM=$('.abiturient-menu');
		var a=$('#abiturient')
		var cMR=$('.college-menu-responsive');
		var cML=$('.college-menu-link');
		var cM=$('.college-menu');
		var c=$('#college')
		var gMR=$('.give-docs-menu-responsive');
		var gML=$('.give-docs-menu-link');
		var gM=$('.give-docs-menu');
		var g=$('#give-docs')
		var sMR=$('.spec-menu-responsive');
		var sML=$('.spec-menu-link');
		var sM=$('.spec-menu');
		var s=$('#spec')
		if(w<768){
			//добавление подменю Абитуриента
			a.click(function(){
				a.toggleClass("_active");
				if(a.hasClass('_active')){
					if(!aMR.hasClass('done')){
						aML.appendTo(aMR);
						aMR.addClass('done');
					}
				} else {
					if(aMR.hasClass('done')){
						aML.appendTo(aM);
						aMR.removeClass('done')
					}			
				}
			});
			//добавление подменю Колледжа
			c.click(function(){
				c.toggleClass("_active");
				if(c.hasClass('_active')){
					if(!cMR.hasClass('done')){
						cML.appendTo(cMR);
						cMR.addClass('done');
					}
				} else {
					if(cMR.hasClass('done')){
						cML.appendTo(cM);
						cMR.removeClass('done')
					}			
				}
			});
			//добавление подменю Подачи документов
			g.click(function(){
				g.toggleClass("_active");
				if(g.hasClass('_active')){
					if(!gMR.hasClass('done')){
						gML.appendTo(gMR);
						gMR.addClass('done');
					}
				} else {
					if(gMR.hasClass('done')){
						gML.appendTo(gM);
						gMR.removeClass('done')
					}			
				}
			});
			//добавление подменю Специальностей
			s.click(function(){
				s.toggleClass("_active");
				if(s.hasClass('_active')){
					if(!sMR.hasClass('done')){
						sML.appendTo(sMR);
						sMR.addClass('done');
					}
				} else {
					if(sMR.hasClass('done')){
						sML.appendTo(sM);
						sMR.removeClass('done')
					}			
				}
			});
		} else {
			//удаление подменю Абитуриента
			if(aMR.hasClass('done')){
				aML.appendTo(aM);
				aMR.removeClass('done')
			}
			//удаление подменю Колледжа
			if(cMR.hasClass('done')){
				cML.appendTo(cM);
				cMR.removeClass('done')
			}
			//удаление подменю Подачи документов
			if(gMR.hasClass('done')){
				gML.appendTo(gM);
				gMR.removeClass('done')
			}
			//удаление подменю Специальностей
			if(sMR.hasClass('done')){
				sML.appendTo(sM);
				sMR.removeClass('done')
			}
		}
}
function adaptive_function() {
		var w=$(window).outerWidth();
		var h=$(window).outerHeight();
	adaptive_header(w,h);
}
adaptive_function();

// =========================================================
// // ================POPUP====================================
// const popupLinks = document.querySelectorAll('.popup-link');
// const lockPadding = document.querySelectorAll('.lock-padding');//


// let unlock = true;

// const timeout = 800;

// // Открыть попап
// if (popupLinks.length > 0) {
// 	for (let index = 0; index < popupLinks.length; index ++) {
// 		const popupLink = popupLinks[index];
// 		popupLink.addEventListener('click', function(e) {
// 			const popupName = popupLink.getAttribute('href').replace('#','');
// 			const curentPopup = document.getElementById(popupName);
// 			popupOpen(curentPopup);
// 			e.preventDefault();
// 		});
// 	}
// }

// // Закрыть попап
// const popupCloseIcon = document.querySelectorAll('.close-popup');
// if(popupCloseIcon.length > 0) {
// 	for (let i = 0; i < popupCloseIcon.length; i++) {
// 		const el= popupCloseIcon[i];
// 		el.addEventListener('click', function(e){
// 			popupClose(el.closest('.popup'));
// 			e.preventDefault();
// 		});
// 	}
// }

// function popupOpen(curentPopup) {
// 	if (curentPopup && unlock) {
// 		const popupActive = document.querySelector('.popup.open');
// 		if(popupActive) {
// 			popupClose(popupActive, false);
// 		} else {
// 			bodyLock();
// 		}
// 		curentPopup.classList.add('open');
// 		curentPopup.addEventListener('click', function(e){
// 			if (!e.target.closest('.popup__content')){
// 				popupClose(e.target.closest('.popup'));
// 			}
// 		});
// 	}
// }

// function popupClose(popupActive, doUnlock = true) {
// 	if (unlock){
// 		popupActive.classList.remove('open');
// 		if (doUnlock) {
// 			bodyUnlock();
// 		}
// 	}
// }

// function bodyLock() {
// 	const lockPaddingValue = window.innerWidth - document.querySelector('.wrapper').offsetWidth + 'px';
// 	if (lockPadding.lenth > 0){
// 		for (let i=0; i<lockPadding.length; i++) {
// 			const el = lockPadding[i]
// 			el.style.paddingRight = lockPaddingValue;
// 		}		
// 	}
// 	body.style.paddingRight = lockPaddingValue;
// 	body.classList.add('lock');

// 	unlock = false;
// 	setTimeout(function() {
// 		unlock = true;
// 	}, timeout);
// }

// function bodyUnlock() {
// 	setTimeout(function(){
// 		if (lockPadding.length > 0){
// 			for (let i = 0; i <lockPadding.length; i++) {
// 				const el = lockPadding[i]
// 				el.style.paddingRight = '0px';
// 			}
// 		}
// 		body.style.paddingRight = '0px';
// 		body.classList.remove('lock');
// 	}, timeout);

// 	unlock = false;
// 	setTimeout(function(){
// 		unlock = true;
// 	}, timeout);
// }

// document.addEventListener('keydown', function (e) {
// 	if(e.which === 27){
// 		const popupActive = document.querySelector('.popup.open');
// 		popupClose(popupActive);
// 	}
// });
// =========================================================