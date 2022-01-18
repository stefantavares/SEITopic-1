const imagesDatabase = "http://127.0.0.1:8000/myimages";
var images = '';


        fetch(imagesDatabase).then(result => {
            return result.json();
            }).then(data=> {
            
            data.forEach(pic => {
            // images+=`<img src='http://localhost:8000/static/images/logos/${pic}' height=50 width=auto>`;
            images+=`<img src='/static/images/logos/${pic}' height=50 width=auto>`;
            });
            document.getElementById("logoRow").innerHTML = images;
            });


// var randomImage; //randomly chosen image

// function getRandom(imagesDatabase) { //Select random image.
//     randomImage = imagesDatabase[Math.floor(Math.random() * imagesDatabase.length)];
// };

// getRandom(imagesDatabase);
// render();

// function render() {
//     document.getElementById("logoRow").innerHTML = '<img src="'+randomImage+'" height=50 width=auto />';
// };
