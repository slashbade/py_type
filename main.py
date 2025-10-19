from dataclasses import dataclass
from prop import Iff, Implies, Prop, modus_ponens, Forall, FreeVar

@dataclass
class Eq(Prop):
    left: object
    right: object

    def __repr__(self):
        return f"({self.left} = {self.right})"

    @staticmethod
    def eq_symm(a: object, b: object) -> Prop:
        return Iff(Eq(a, b), Eq(b, a))

    @staticmethod
    def eq_trans(a: object, b: object, c: object) -> Implies:
        return Implies(Implies(Eq(a, b), Eq(b, c)), Eq(a, c))

    @staticmethod
    def eq_refl(a: object) -> Prop:
        return Eq(a, a)

    @staticmethod
    def eq_ext(f, a1: object, a2: object) -> Implies:
        return Implies(Eq(a1, a2), Eq(f(a1), f(a2)))

@dataclass
class Nat:
    def __add__(self, other: 'Nat') -> 'Nat':
        return add(self, other)

@dataclass
class Succ(Nat):
    pred: Nat
    def __repr__(self):
        return f"S({self.pred})"    

@dataclass
class Zero(Nat):
    def __repr__(self):
        return "0"

def eq(n1: Nat, n2: Nat) -> Prop:
    return Eq(n1, n2)

def add(n1: Nat, n2: Nat) -> Nat:
    match n1:
        case Zero():
            return n2
        case Succ(pred):
            return Succ(add(pred, n2))
        case _:
            raise ValueError("Invalid `Nat` value")

def zero_add(b: Nat) -> Prop:
    return Eq(add(Zero(), b), b)

def add_comm(a: Nat, b: Nat) -> Prop:
    return Eq(a + b, b + a)

def one_add_two_three() -> Prop:
    return Eq(one + two, three)

one = Succ(Zero())
two: Nat = Succ(one)
three: Nat = Succ(two)
four: Nat = Succ(three)
six: Nat = Succ(Succ(four))

def prove_one_add_two_eq_three() -> None:
    proof = modus_ponens(
        Eq.eq_ext(Succ, Zero(), Zero()), 
        Eq.eq_refl(Zero())
    )
    proof = modus_ponens(
        Eq.eq_ext(Succ, Succ(Zero()), Succ(Zero())),
        proof
    )
    proof = modus_ponens(
        Eq.eq_ext(Succ, Succ(Succ(Zero())), Succ(Succ(Zero()))),
        proof
    )
    print(proof == one_add_two_three())

def prove_add_comm(a: Nat, b: Nat) -> None:
    match a:
        case Zero():
            assert zero_add(b) == add_comm(a, b)
        case _:
            pass
            
            
            
            

def main():
    prove_one_add_two_eq_three()


if __name__ == "__main__":
    main()
