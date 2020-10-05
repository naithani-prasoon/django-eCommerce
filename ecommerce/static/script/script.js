function displayTab(evt, tabName) {
  var i, number_of_tabs, number_of_divnumber_of_div;
  number_of_tabs = document.getElementsByClassName("accountTabs");
  for (i = 0; i < number_of_tabs.length; i++) {
    number_of_tabs[i].style.display = "none";
  }
  number_of_div = document.getElementsByClassName("accountTab");

  for (i = 0; i < number_of_div.length; i++) {
    number_of_div[i].className = number_of_div[i].className.replace(" active", "");
  }
  document.getElementById(tabName).style.display = "flex";
  evt.currentTarget.className += " active";
}

document.getElementById('accountDefault').click()
