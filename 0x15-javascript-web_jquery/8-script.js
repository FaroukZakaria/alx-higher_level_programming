$(document).ready(function(){
	$.ajax({
		url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
		method: 'GET',
		success: function(response) {
			const movies = response.results;
			const list = $('UL#list_movies');
			movies.forEach(function(movie) {
				list.append('<li>' + movie.title + '</li>');
			});
		},
		error: function(error) {
			console.error(error);
		}
	});
});
