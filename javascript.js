var url = "http://127.0.0.1:5000/view";
var id = "view";

async function generator(url, id) {
    var request = await new XMLHttpRequest()

request.open('GET', url, true)
request.onload = function () {
  // Begin accessing JSON data here
  var data = JSON.parse(this.response)
view(data, request, id);

}

request.send()
  }

  function view(data, request, id){
    if (request.status >= 200 && request.status < 400) {
         data.forEach((query) => {
          console.log(request.status);
          var div = document.createElement("div");
            var mainContainer = document.getElementById(id);
          div.innerHTML = "<h5>"+query.id+"</h5><h6>"+query.name+"</h6><p>"+ query.email +"</p><hr>";
          mainContainer.appendChild(div)
        })
      } else {
        console.log('error')
      }
  }

async function generate_html(){
await generator(url, id);
}

generate_html();