function readFiles(files,callback,index=0) {
    if (files && files[0]) {
      let file = files[index++],
          reader = new FileReader();
      reader.onload = function(e){
        callback(e);
        if(index<files.length) readFiles(files,callback,index);
      }
      reader.readAsDataURL(file);
    }
  }

  // Create a selector for an input and then do whatever you want using the callback function.
$("body")
    .on("change",".imagepicker-replace input",function() {
    // store the current "this" into a variable
    var imagepicker = this;
    readFiles(this.files,function(e) {
    // "this" will be different in the callback function
    $(imagepicker).parent()
        .addClass("picked")
        .css({"background-image":"url("+e.target.result+")"});
    });
})



// This example will add a new thumbnail each time
$("body")
    .on("change",".imagepicker-add input",function() {
    var imagepicker = this;
    readFiles(this.files,function(e) {
        $(imagepicker).parent().before(
            "<div class='thumbnail' style='background-image:url("+e.target.result+")'></div>"
        )
    });
});