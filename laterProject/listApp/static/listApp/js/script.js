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
    document.getElementById('id_author_first_name').value=command;
    document.getElementById('id_author_last_name').value=command;
    document.getElementById('id_book_title').value=command;
    // id_author_first_name.innerHTML = 'Voice Input: ' + command + '.';
    // id_author_last_name.innerHTML = 'Voice Input: ';
    // id_book_title.innerHTML = 'Voice Input: ';


//     $(document).on('submit', '#post-book',function(e){
//       // e.preventDefault();
//       // id_<field_name>
//       // id_author_first_name
//       // id_author_last_name
//       // id_book_title
//       $.ajax({
//           type:'POST',
//           url:'{% url "listApp/new/" %}',
//           data: {
//               author_first_name: 'hi',   // converts js value to JSON string
//               author_last_name: 'Ortega',
//               book_title: 'Vintage'
//             },
//           success:function(json){
//               document.getElementById("post-book").reset();
//           },
//           error : function(xhr,errmsg,err) {
//           console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
//       }
//       });
// });

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
