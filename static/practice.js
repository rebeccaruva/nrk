
// Create a "close" button and append it to each list item
var myNodelist = document.getElementsByTagName("li");
var i;
for (i = 0; i < myNodelist.length; i++) {
  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  myNodelist[i].appendChild(span);
}

// Click on a close button to hide the current list item
var close = document.getElementsByClassName("close");
var i;
for (i = 0; i < close.length; i++) {
  close[i].onclick = function() {
    var div = this.parentElement;
    div.style.display = "none";
  }
}

// Add a "checked" symbol when clicking on a list item
var list = document.querySelector('ul');
list.addEventListener('click', function(ev) {
  if (ev.target.tagName === 'li') {
    ev.target.classList.toggle('checked');
  }
}, false);

// Create a new list item when clicking on the "Add" button
function SundayElement() {
  var li = document.createElement("li");
  var inputValue = document.getElementById("Sunday").value;
  var t = document.createTextNode(inputValue);
  li.appendChild(t);
  if (inputValue === '') {
    alert("Write something, you can do it!");
  } else {
    document.getElementById("sunday").appendChild(li);
  }
  document.getElementById("Sunday").value = "";

  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  li.appendChild(span);

  for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
      var div = this.parentElement;
      div.style.display = "none";
    }
  }
}

// Create a new list item when clicking on the "Add" button
function MondayElement() {
  var li = document.createElement("li");
  var inputValue = document.getElementById("Monday").value;
  var t = document.createTextNode(inputValue);
  li.appendChild(t);
  if (inputValue === '') {
    alert("Write something, you can do it!");
  } else {
    document.getElementById("monday").appendChild(li);
  }
  document.getElementById("Monday").value = "";

  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  li.appendChild(span);

  for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
      var div = this.parentElement;
      div.style.display = "none";
    }
  }
}


// Create a new list item when clicking on the "Add" button
function TuesdayElement() {
  var li = document.createElement("li");
  var inputValue = document.getElementById("Tuesday").value;
  var t = document.createTextNode(inputValue);
  li.appendChild(t);
  if (inputValue === '') {
    alert("Write something, you can do it!");
  } else {
    document.getElementById("tuesday").appendChild(li);
  }
  document.getElementById("Tuesday").value = "";

  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  li.appendChild(span);

  for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
      var div = this.parentElement;
      div.style.display = "none";
    }
  }
}



// Create a new list item when clicking on the "Add" button
function WednesdayElement() {
  var li = document.createElement("li");
  var inputValue = document.getElementById("Wednesday").value;
  var t = document.createTextNode(inputValue);
  li.appendChild(t);
  if (inputValue === '') {
    alert("Write something, you can do it!");
  } else {
    document.getElementById("wednesday").appendChild(li);
  }
  document.getElementById("Wednesday").value = "";

  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  li.appendChild(span);

  for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
      var div = this.parentElement;
      div.style.display = "none";
    }
  }
}




// Create a new list item when clicking on the "Add" button
function ThursdayElement() {
  var li = document.createElement("li");
  var inputValue = document.getElementById("Thursday").value;
  var t = document.createTextNode(inputValue);
  li.appendChild(t);
  if (inputValue === '') {
    alert("Write something, you can do it!");
  } else {
    document.getElementById("thursday").appendChild(li);
  }
  document.getElementById("Thursday").value = "";

  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  li.appendChild(span);

  for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
      var div = this.parentElement;
      div.style.display = "none";
    }
  }
}



// Create a new list item when clicking on the "Add" button
function FridayElement() {
  var li = document.createElement("li");
  var inputValue = document.getElementById("Friday").value;
  var t = document.createTextNode(inputValue);
  li.appendChild(t);
  if (inputValue === '') {
    alert("Write something, you can do it!");
  } else {
    document.getElementById("friday").appendChild(li);
  }
  document.getElementById("Friday").value = "";

  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  li.appendChild(span);

  for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
      var div = this.parentElement;
      div.style.display = "none";
    }
  }
}

// Create a new list item when clicking on the "Add" button
function SaturdayElement() {
  var li = document.createElement("li");
  var inputValue = document.getElementById("Saturday").value;
  var t = document.createTextNode(inputValue);
  li.appendChild(t);
  if (inputValue === '') {
    alert("Write something, you can do it!");
  } else {
    document.getElementById("saturday").appendChild(li);
  }
  document.getElementById("Saturday").value = "";

  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  li.appendChild(span);

  for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
      var div = this.parentElement;
      div.style.display = "none";
    }
  }
}
