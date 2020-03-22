function bookSearch(e){
  e.preventDefault()
  console.log('this function runs');
  // location.href="{% url 'book-detail' object.id %}"
  // var a = "{{ object.book_title }}";
  // console.log('a', a);
  // var search = 'Becoming';
  var search = document.getElementById('id_book_title_or_author_name').value;
  document.getElementById('results').innerHTML = "";

  $.ajax({
    url: "https://www.googleapis.com/books/v1/volumes?q=" + search,
    dataType: "json",
    type:'GET',
    success: function(data) {

      for(i=0; i<data.items.length; i++) {

        results.innerHTML += "<h2>" + "Title: " + data.items[i].volumeInfo.title + "</h2>";
        results.innerHTML += "<h2>" + "Authors: " + data.items[i].volumeInfo.authors + "</h2>";
        results.innerHTML += "<img src=" + data.items[i].volumeInfo.imageLinks.thumbnail + "/>";
        results.innerHTML += "<h2>" + "Published Date: " + data.items[i].volumeInfo.publishedDate + "</h2>";
        results.innerHTML += "<h2>" + "Publisher: " + data.items[i].volumeInfo.publisher + "</h2>";
        results.innerHTML += "<h2>" + "Description: " + data.items[i].volumeInfo.description + "</h2>";
        console.log("result not string----------");
        console.log(data.items[i]);
        var result_string = JSON.stringify(data.items[i]);
        console.log("result_string>>>>>>>");
        console.log(result_string);
        console.log("result to string ++++++++++++++");
        console.log(data.items[i].toString());

        // creating a button
        results.innerHTML += "<button type='button' onclick='selectBook(" + result_string + ")'>Add</button>";



      }
    }
  });

}

document.getElementById('save-btn').addEventListener("click", bookSearch)

function selectBook(data) {
  console.log("Hello World");
  console.log("accepting data");
  console.log(data);
  data_parsed = JSON.parse(data)

  function getCookie(name) {

  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
  }

  var csrftoken = getCookie('csrftoken');
  var jsonString = JSON.stringify(data_parsed);
  var xhttp = new XMLHttpRequest();
  xhttp.open("POST", "/listApp/new/", true);
  xhttp.responseType = "json";
  xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xhttp.setRequestHeader("X-CSRFToken", csrftoken);
  xhttp.send(jsonString);
}
