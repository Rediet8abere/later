function bookSearch(e){
  e.preventDefault()
  console.log('this function runs');
  // location.href="{% url 'book-detail' object.id %}"
  // var a = "{{ object.book_title }}";
  // console.log('a', a);
  // var search = 'Becoming';
  var search = document.getElementById('id_author_name').value;
  document.getElementById('results').innerHTML = "";

  $.ajax({
    url: "https://www.googleapis.com/books/v1/volumes?q=" + search,
    dataType: "json",
    success: function(data) {
      for(i=0; i<data.items.length; i++) {
        // console.log(data.items[i].volumeInfo.title)
        results.innerHTML += "<h2>" + data.items[i].volumeInfo.title + "</h2>";
        results.innerHTML += "<h2>" + data.items[i].volumeInfo.authors + "</h2>";
        results.innerHTML += "<img src=" + data.items[i].volumeInfo.imageLinks.thumbnail + "/>";


      }
    },
    type:'GET'
  });

}

document.getElementById('save-btn').addEventListener("click", bookSearch)
