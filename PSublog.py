% Semantic constructs

% Autonomous word
word(ListOfChars, Word):-
	w(ListOfChars),
	list_to_word(ListOfChars, Word).
	
% Substring in word	
in_word(ListOfChars, Word):-
	w(List),
	append(ListOfChars, _, ListTemp),
	append(_, ListTemp, List),
	
	list_to_word(List, Word).

% Prefix of word	
prefix(ListOfChars, Word):-
	w(List),
	append(ListOfChars, _ , List),
	list_to_word(List, Word).

% Substring of word
sufix(ListOfChars, Word):-
	w(List),
	append(_, ListOfChars, List),
	list_to_word(List, Word).


	
	
% Utilities	

% Join char array to string
list_to_word(ListOfChars, Word):-
	atomic_list_concat(ListOfChars, '', Atom), 
	atom_string(Atom, Word).

% Elements of array are distinct 
alldif([]).
alldif([E|Es]):-
   maplist(dif(E), Es),
   alldif(Es).
   
% Join words array to string
join_words(Words, Statement):-
	insert_spaces(Words, OutWords),
	with_output_to(
					atom(Statement), 
					maplist(write, OutWords)
				   ).
				   
% Format words as statement
insert_spaces([],[]):- !.
insert_spaces([A], [A,'\n']):- !.
insert_spaces([Word | Rest], OutWords):-
	insert_spaces(Rest, OutWordsRest),
	OutWords = [Word, " " | OutWordsRest].

% Concatenate elements of lists to one list
join_lists([],[]).
join_lists([H|T], List):-
	join_lists(T, TempList),
	append(H, TempList, List).
	
% Build set of elements of list of lists
unique_elements(ListOfLists, Set):-
	join_lists(ListOfLists, GiantList),
	list_to_set(GiantList, Set).

	
	
	
	
	
% Definition of solution
solution(Solution):-
	% The line group order affects the correctness!
	
	% format of words
	F1 = [Vklicaj, V8, V5, VC],
	F2 = [V7, V5, V9],
	F3 = [V3, V9, V5],
	F4 = [VC, VN],
		
	% apply semantic constructs
	word(F1, W1), 
	word(F2, W2), 
	word(F3, W3),
	word(F4, W4), 
	
	
	% different chars
	unique_elements([F1, F2, F3, F4], Uniques),
	alldif(Uniques),
	
	% lock variable to specific list of chars
	member(V7, [a, e, i, o]),
	not(member(V5, [a, e, i, o])),
	
	
	
	% join words to statement
	join_words([W1, W2, W3, W4], Solution).
	
	
	
% Write all solutions to text file
program:-
	open('C:/Users/User/Desktop/izhod.txt', write, Stream),
	forall(solution(S), write(Stream, S)),
	close(Stream).
	
	
