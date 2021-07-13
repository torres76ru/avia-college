// ==========================Calendar==========================================
function Calendar2(id, year, month) {
var Dlast = new Date(year,month+1,0).getDate(),
    D = new Date(year,month,Dlast),
    M = "",
    DNlast = new Date(D.getFullYear(),D.getMonth(),Dlast).getDay(),
    DNfirst = new Date(D.getFullYear(),D.getMonth(),1).getDay(),
    calendar = '<tr>',
    month=["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"];
if (DNfirst != 0) {
  for(var  i = 1; i < DNfirst; i++) calendar += '<td>';
}else{
  for(var  i = 0; i < 6; i++) calendar += '<td>';
}
for(var  i = 1; i <= Dlast; i++) {
    //Загрузка каждой даты поэлементно
    if (check_date(D.getFullYear() + '-' + D.getMonth() + '-' + i)){
      if (i == new Date().getDate() && D.getFullYear() == new Date().getFullYear() && D.getMonth() == new Date().getMonth()) {
        calendar += '<td class = "today date-o" onclick="var date = \'' + D.getFullYear() + '-' + D.getMonth() + '-' + i  + '\'; format_date(date); return false;">' + i + '</td>';
      } else{
        calendar += '<td class = "date-o" onclick="var date = \'' + D.getFullYear() + '-' + D.getMonth() + '-' + i  + '\'; format_date(date); return false;">' + i + '</td>';
      }

		} else {
      if (i == new Date().getDate() && D.getFullYear() == new Date().getFullYear() && D.getMonth() == new Date().getMonth()) {
        calendar += '<td class="today date-c">' + i;
      } else {
        calendar += '<td class = "date-c">' + i + '</td>';
      }
		}
  if (new Date(D.getFullYear(),D.getMonth(),i).getDay() == 0) {
    calendar += '<tr>';
  }
}
for(var  i = DNlast; i < 7; i++) calendar += '<td>&nbsp;';
document.querySelector('#'+id+' tbody').innerHTML = calendar;
document.querySelector('#'+id+' thead td:nth-child(2)').innerHTML = month[D.getMonth()] +' '+ D.getFullYear();
document.querySelector('#'+id+' thead td:nth-child(2)').dataset.month = D.getMonth();
document.querySelector('#'+id+' thead td:nth-child(2)').dataset.year = D.getFullYear();
if (document.querySelectorAll('#'+id+' tbody tr').length < 6) {  // чтобы при перелистывании месяцев не "подпрыгивала" вся страница, добавляется ряд пустых клеток. Итог: всегда 6 строк для цифр
    document.querySelector('#'+id+' tbody').innerHTML += '<tr><td>&nbsp;<td>&nbsp;<td>&nbsp;<td>&nbsp;<td>&nbsp;<td>&nbsp;<td>&nbsp;';
}
}
Calendar2("calendar2", new Date().getFullYear(), new Date().getMonth());
// переключатель минус месяц
document.querySelector('#calendar2 thead tr:nth-child(1) td:nth-child(1)').onclick = function() {
  Calendar2("calendar2", document.querySelector('#calendar2 thead td:nth-child(2)').dataset.year, parseFloat(document.querySelector('#calendar2 thead td:nth-child(2)').dataset.month)-1);
}
// переключатель плюс месяц
document.querySelector('#calendar2 thead tr:nth-child(1) td:nth-child(3)').onclick = function() {
  Calendar2("calendar2", document.querySelector('#calendar2 thead td:nth-child(2)').dataset.year, parseFloat(document.querySelector('#calendar2 thead td:nth-child(2)').dataset.month)+1);
}

function format_date(date){
	var date_arr = date.split('-');
	date_arr[1]++;
	date_arr[1] = "" + date_arr[1];
  $.each($('.date-o'), function (index, val) {
    if ($(this).text() == date_arr[2]){
      $(this).addClass('date-active');
    } else {
      $(this).removeClass('date-active');
    }
  });
  $.each($('.q-time'), function (index, val) {
      $(this).removeClass('q-time-active');
  });
	if(date_arr[1].length<2)date_arr[1] = '0' + date_arr[1];
	if(date_arr[2].length<2)date_arr[2] = '0' + date_arr[2];
	document.getElementById('id_date').value = date_arr[0] + '-' + date_arr[1] + '-' + date_arr[2];
  $.each($('.q-time'), function (index, val) {
    if (check_time($(this).text())) {
      $(this).addClass('q-time_o');
    } else {
      $(this).removeClass('q-time_o');
    }
  });

  $('#q-submit').addClass('q-submit');
}


function add_time(time){
  $.each($('.q-time'), function (index, val) {
    if ($(this).attr("class") == "q-time q-time_o" && ($(this).text() + ":00") == time) {
      var dateTime = document.getElementById('id_date').value
      dateTime_arr = dateTime.split(' ');
      dateTime_arr[1] = time;
      document.getElementById('id_date').value = dateTime_arr[0] + ' ' + dateTime_arr[1];
      $('#q-submit').removeClass('q-submit');
      $(this).addClass("q-time-active");
    } else {
      $(this).removeClass("q-time-active");
    }
  });
	
}

function check_date(date){
	var date_arr = date.split('-');
	date_arr[1]++;
	date_arr[1] = "" + date_arr[1];
	if(date_arr[1].length<2)date_arr[1] = '0' + date_arr[1];
	if(date_arr[2].length<2)date_arr[2] = '0' + date_arr[2];
  for (i in dtf_arr) {
		if(dtf_arr[i].includes(date_arr[0] + '-' + date_arr[1] + '-' + date_arr[2])){
			return true;
		}
	}
}

function check_time(time){
  var dateTime = document.getElementById('id_date').value
  dateTime_arr = dateTime.split(' ');
  for (i in dtf_arr) {
    if(dtf_arr[i].includes(dateTime_arr[0])){
      if(dtf_arr[i].includes(time +':00')){
        return true;
      }
    }
  }
}