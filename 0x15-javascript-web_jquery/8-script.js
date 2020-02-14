$.ajax({
  url: 'https://swapi.co/api/films/?format=json',
  type: 'GET',
  dataType: 'json'
}).done(function (json) {
  const movies = json.results;
  for (let i = 0; i < movies.length; i++) {
    $('UL#list_movies').append('<li>' + movies[i].title + '</li>');
  }
});
