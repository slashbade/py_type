from prop import Prop

class Forall(Prop):
    var: object
    body: Prop
    
    def __repr__(self):
        return f"∀{self.var}.({self.body})"