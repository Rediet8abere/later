console.log('Hello Rediet Abere');
var message = document.querySelector('#message');

var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition;
var SpeechGrammarList = SpeechGrammarList || webkitSpeechGrammarList;

var grammar = '#JSGF V1.0;'

var recognition = new SpeechRecognition();
var speechRecognitionList = new SpeechGrammarList();
speechRecognitionList.addFromString(grammar, 1);
recognition.grammars = speechRecognitionList;
recognition.lang = 'en-US';
recognition.interimResults = false;

recognition.onresult = function(event) {
    var last = event.results.length - 1;
    var command = event.results[last][0].transcript;
    var d = {};
    d['text'] = command
    console.log('Hello j cole!');
    console.log('command', command);
    console.log("d", d['text']);
    message.textContent = 'Voice Input: ' + command + '.';

    $(document).on('submit', '#post-book',function(e){
      e.preventDefault();
      $.ajax({
          type:'POST',
          url:'{% url "listApp/new/" %}',
          data: {
              author_first_name: 'hi',   // converts js value to JSON string
              author_last_name: 'Ortega',
              book_title: 'Vintage'
            },
          success:function(json){
              document.getElementById("post-book").reset();
              // $(".posts").prepend('<div class="col-md-6">'+
              //     '<div class="row no-gutters border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">' +
              //         '<div class="col p-4 d-flex flex-column position-static">' +
              //             '<h3 class="mb-0">' + json.author_first_name + '</h3>' +
              //             '<p class="mb-auto">' + json.author_last_name + '</p>' +
              //         '</div>' +
              //     '</div>' +
              // '</div>'
              // )
          },
          error : function(xhr,errmsg,err) {
          console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
      }
      });
});
    // $.ajax({
    //
    // // location.href = Flask.url_for('index', {});
    //   type: 'POST',
    //   url: '/listApp/new/',
    //   data: {
    //     author_first_name: 'hi',   // converts js value to JSON string
    //     author_last_name: 'Ortega',
    //     book_title: 'Vintage'
    //   },
    //   processData: true,
    //   success:function(response)
    //   {
    //   }
    //
    //   })
      // author_first_name = models.CharField(max_length=30)
      //   author_last_name = models.CharField(max_length=30)
      //   book_title = models.CharField(max_length=60)
      //   list_pub_date = models.DateTimeField(default=timezone.now)


};

recognition.onspeechend = function() {
    recognition.stop();
};

recognition.onerror = function(event) {
    message.textContent = 'Error occurred in recognition: ' + event.error;
}

document.querySelector('#btnGiveCommand').addEventListener('click', function(){
    recognition.start();

});
