/*global console*/
var likeIcon = document.getElementById("like"),
    likeCounter = likeIcon.nextElementSibling,
    loveIcon = document.getElementById("love"),
    loveCounter = loveIcon.nextElementSibling,
    comment = document.getElementById("comment"),
    addComment = comment.nextElementSibling,
    commentsContainer = document.getElementById("comments-container"),
    commentCounter = document.getElementById("comment-counter");

likeIcon.addEventListener("click", function () {
    this.classList.toggle("like");
    var numberOfLikes = Number(likeCounter.textContent);
    if (this.classList.contains("like")) {
        numberOfLikes++;
        likeCounter.textContent = numberOfLikes;
    } else {
        numberOfLikes--;
        likeCounter.textContent = numberOfLikes;
    }
});

loveIcon.addEventListener("click", function () {
    this.classList.toggle("love");
    var numberOfLoves = Number(loveCounter.textContent);
    if (this.classList.contains("love")) {
        numberOfLoves++;
        loveCounter.textContent = numberOfLoves;
    } else {
        numberOfLoves--;
        loveCounter.textContent = numberOfLoves;
    }
});

addComment.addEventListener("click", function () {

    if(comment.value) {
        var numberOfComments = Number(commentCounter.textContent),
            date = new Date();
            numberOfComments++;
            commentCounter.textContent = numberOfComments;
            commentsContainer.style.display = "block";
            commentsContainer.innerHTML +=
            `<div>
                <img src="static/img/igor.jpg" class="img-fluid avatar avt-comment" alt="Igor Brown">
                ${comment.value}
              <span>${date.toLocaleDateString()} às ${date.toLocaleTimeString().replace(/(.*)\D\d+/, '$1')} </span>
              <i class="fa fa-trash"></i>
            </div>`;
        comment.value = "";
        var deleteIcons = document.querySelectorAll(".container .comments div i");
        for (let i = 0; i < deleteIcons.length; i++) {
            deleteIcons[i].addEventListener("click", function () {
                this.parentElement.style.display = "none";
                numberOfComments--;
                commentCounter.textContent = numberOfComments;
            });
        }
    }
    else {
        alert('Preencha o campo com seu comentário.');
    }
  

    console.log('comentou');
    setTimeout(() => {
      window.scrollTo(0,document.body.scrollHeight);
    }, 200);
  

});


// get input 
var input = document.getElementById("comment");

input.addEventListener("keyup", function(event) {
  // number 13 is the "Enter" key on the keyboard
  if (event.keyCode === 13) {
    event.preventDefault();
    document.getElementById("add-comment").click();
  }
});
