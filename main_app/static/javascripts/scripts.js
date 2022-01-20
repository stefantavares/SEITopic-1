const imagesDatabase = "/myimages";
var images = '';


        fetch(imagesDatabase).then(result => {
            return result.json();
            }).then(data=> {
                console.log(data);
            data.forEach(pic => {
            images+=`<img src='/static/images/logos/${pic}' height=50 width=auto>`;
            });
            document.getElementById("logoRow").innerHTML = images;
            });


