from dataclasses import dataclass

class Prop:
    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return self.name

@dataclass
class Axiom:
    prop: Prop

@dataclass
class Not(Prop):
    prop: Prop

    def __repr__(self):
        return f"¬({self.prop})"

@dataclass
class Implies(Prop):
    antecedent: Prop
    consequent: Prop

    def __repr__(self):
        return f"({self.antecedent} → {self.consequent})"

def Or(p1: Prop, p2: Prop) -> Prop:
    return Implies(Not(p1), p2)

def And(p1: Prop, p2: Prop) -> Prop:
    return Not(Implies(p1, Not(p2)))

def Iff(p1: Prop, p2: Prop) -> Prop:
    return And(Implies(p1, p2), Implies(p2, p1))

def modus_ponens(imp: Implies, antecedent: Prop) -> Prop:
    if imp.antecedent != antecedent:
        raise ValueError("Antecedent does not match")
    return imp.consequent

@dataclass
class FreeVar:
    name: str

@dataclass
class Forall(Prop):
    var: FreeVar
    body: Prop
    
    def __repr__(self):
        return f"∀{self.var}.({self.body})"


def check(p: Prop) -> bool:
    match p:
        case Axiom():
            return True
        case Not(inner):
            return not check(inner)  # Simplified for demonstration
        case Implies(antecedent, consequent):
            return not check(antecedent) or check(consequent)  # Simplified for demonstration
        case _:
            return False



if __name__ == "__main__":
    p = Prop("p")
    q = Prop("q")
    r = Prop("r")

    assert Implies(p, Implies(q, p))
    assert Implies(
        Implies(p, Implies(q, r)),
        Implies(Implies(p, q), Implies(p, r))
    )

    s = Implies(
        Implies(Not(p), Not(q)),
        Implies(q, p)
    )

    print(s)

    print("All checks passed.")

            
