
var this_thing = "thing";

var my_array = ["something", "another", 10, this_thing];

console.log(my_array);

function get_random_number( max_number ){
  var random_number = Math.random() * max_number;
  random_number = Math.ceil(random_number);
  return random_number;
}

// var some = get_random_number( 3 );


console.log( my_array[ get_random_number(3) ] )