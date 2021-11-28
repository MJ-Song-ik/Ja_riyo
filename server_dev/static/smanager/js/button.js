function count(type, id)  {
    const resultElement = document.getElementById(id);
    let number = parseInt(resultElement.value);
  
    if(type === "plus") {
      number = number + 1;
    }else if(type === "minus")  {
      number = number - 1;
    }
    resultElement.value= number;
  }