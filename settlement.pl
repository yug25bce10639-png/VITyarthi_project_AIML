% Rule: A person is a debtor if their balance is negative
debtor(Person, Amount) :- balance(Person, Amount), Amount < 0.

% Rule: A person is a creditor if their balance is positive
creditor(Person, Amount) :- balance(Person, Amount), Amount > 0.

% Rule: Suggest a transfer if X owes money and Y is owed money
suggest_transfer(From, To) :-
    debtor(From, _),
    creditor(To, _),
    From \= To.
