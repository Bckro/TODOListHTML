document.getElementById("add-btn").addEventListener("click", function()
{
   const newTask = document.getElementById("task").value;

  if(newTask == "")
  {
    document.getElementById("msg").innerHTML = "Uzupełnij pole!";
  }
  else {
    document.getElementById("tasks-list").innerHTML += "<li>" + newTask + "</li>";
    document.getElementById("task").value = "";
    document.getElementById("msg").value="";
  }
}
);

document.getElementById("tasks-list").addEventListner("click",function(e){
  const task = e.target;
  this.removeChild(task);
})