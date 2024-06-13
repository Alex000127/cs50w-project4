document.addEventListener('DOMContentLoaded', function() {
    console.log("Funciona")
 
    post = document.querySelectorAll('.container-post')
    for (let i = 0; i < post.length; i++) {
        post[i].style.cursor = "pointer";
      }
    
})



function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(";").shift();
    return null; // En caso de que no se encuentre la cookie
  }

function submitHandler(id) {
const textareaValue = document.getElementById(`textarea_${id}`).value;
fetch(`/edit/${id}`, {
    method: "POST",
    headers: {
    "Content-type": "application/json",
    "X-CSRFToken": getCookie("csrftoken"),
    },
    body: JSON.stringify({
    content: textareaValue,
    }),
})
    .then((response) => {
    if (!response.ok) {
        throw new Error("Network response was not ok");
    }
    // Recargar la página después de la edición
    location.reload();
    })
    .catch((error) => {
    console.error("Error:", error);
    });
}

function likeHandler(id, isLiked) {
const btn = document.getElementById(`like-btn-${id}`);
const likeCountElem = document.getElementById(`like-count-${id}`);
const action = "addLIKE";

fetch(`/${action}/${id}`, {
    method: "POST",
    headers: {
    "Content-type": "application/json",
    "X-CSRFToken": getCookie("csrftoken"),
    },
})
    .then((response) => response.json())
    .then((data) => {
    console.log(likeCountElem)
    if (data.liked !== undefined) {
        console.log(data);
        btn.textContent = data.liked ? "No Me Gusta" : "Me Gusta";
        // btn.onclick = () => likeHandler(id, data.liked);
        likeCountElem.innerHTML =data.like_count
    } else {
        console.error("Unexpected response:", data);
    }
    })
    .catch((error) => {
    console.log("Error:", error);
    });
}