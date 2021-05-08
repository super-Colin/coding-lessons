// It's hard to do anything without variables and functions
// So I just want to make sure we all have a decent understanding of the basics
// If we cruise through all this we'll.... figure out something cool to aim towards

// _______________________________________________________
// -------------------------------------------------------

// Variables

// Variables are reusable chunks of data assigned to a label
var my_variable = 42;
console.log(my_variable); // should print 42 to the console

// Data inside the variable can be changed or passed to another variable
my_variable = 10;
var should_be_ten = my_variable;
console.log(should_be_ten); // should print 10 now

// ..Unless the variable is decraled as a "Constant" when it is created
const my_constant = "This can NOT be changed";
console.log(my_constant);

my_constant = "Something else"; // Will produce an error
console.log(my_constant);



// ______________________________________________________
// ------------------------------------------------------

// Functions 

// a function is a reusable set of instructions or operations assigned to a label
function my_function(){
  console.log("This is my function");
}
my_function(); //Should print "This is my function"

// functions can take "arguments" or "parameters" to control their behavior
function needs_argument( required_chunk_of_data ){
  console.log( required_chunk_of_data );
}
needs_argument( "Here's some yummy data to work with" );


// functions normally "return" some sort of data back
function returns_one(){
  return 1;
}
returns_one(); // "return" will not print anything to the console

//  but the returned data is easily stored in a variable to use later
var functions_output = returns_one();
console.log(functions_output);




// When we combine variables and functions things start getting fun 

var the_input = 20;

function add_seven( expected_number_parameter ){
  return expected_number_parameter + 7;
}

var the_answer = add_seven(the_input);

console.log("The answer is " + the_answer);




