// 5 star widget

let stars = document.querySelectorAll(".ratings span");
let products = document.querySelectorAll(".ratings");
let ratings = [];

//for each click on the stars, we mark them so that css highlights all the stars till that star
//Also, when a star is clicked, rating and product-id is stored in localstorage. This could be sent to database as well.
for (let star of stars){
    star.addEventListener("click", function () {
        let children = Array.from(star.parentElement.children).reverse()
        for (let child of children){
            if (child.getAttribute("data-clicked")){
                return false
            }
        }
        for (let child of children){
            child.innerHTML= "&#9733"
            child.setAttribute("style","color: black;")
            if(this == child){
                this.setAttribute("data-clicked","true");
                break
            }
        }
        let rating = this.dataset.rating;
        let productId = this.parentElement.dataset.productid;
        let data = {
            "productId": productId,
            "stars": rating
        }
        ratings.push(data);
        localStorage.setItem("rating",JSON.stringify(ratings));
    });


    //set hover color to grey and change to solid star
    star.addEventListener("mouseover", function () {
        let children = Array.from(star.parentElement.children).reverse()
        for (let child of children){
            if (child.getAttribute("data-clicked")){
                return false
            }
        }
        for (let child of children){
            child.innerHTML= "&#9733"
            child.setAttribute("style","color: grey;")
            if(this == child){
                break
            }
        }
    })

    //set hover color back and chage star to shallow
    star.addEventListener("mouseout", function () {
        let children = Array.from(star.parentElement.children).reverse()
        for (let child of children){
            if (child.getAttribute("data-clicked")){
                return false
            }
        }
        for (let child of children){
            child.innerHTML= "&#9734"
            child.setAttribute("style","color: black;")
            if(this == child){
                break
            }
        }
    })
}

//This checks if a users has already rated, those ratings are displayed across reloads
if(localStorage.getItem("rating")){
    ratings = JSON.parse(localStorage.getItem("rating"));
    for (let rating of ratings){
        for (let product of products){
            if (rating["productId"] == product.dataset.productid){
                let reverseStars = Array.from(product.children).reverse();
                let index = parseInt(rating["stars"])-1;
                for(let i = 0; i <= index; i++){
                   reverseStars[i].innerHTML= "&#9733"
                   reverseStars[i].setAttribute("data-clicked","true");
                }
            }                
        }
    }
}


