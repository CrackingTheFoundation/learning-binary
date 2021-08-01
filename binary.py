from manim import *

class LearningBinary(Scene):
    def construct(self):
        
        intro_1=Text("Can you teach children binary").shift(UP*.5)
        intro_2=Text("arithmetic by only asking questions?").shift(DOWN*.5)
        intro = VGroup(intro_1, intro_2)
        self.add(intro)
        self.wait(3)
        
        reenactment_1 = Text("The following is a reenactment of").shift(UP)
        reenactment_2 = Text("a learning session with real third")
        reenactment_3 = Text("grade children.").shift(DOWN)
        reenactment = VGroup(reenactment_1, reenactment_2, reenactment_3)
        self.play(Transform(intro,reenactment))
        self.wait(2)
        
        self.play(FadeOut(intro), run_time=2)
        
        child1_confused = SVGMobject("assets/confused.svg")
        child1_sleepy = SVGMobject("assets/sleepy.svg")
        child1_excited = SVGMobject("assets/excited.svg")
        child1_skeptical = SVGMobject("assets/skeptical.svg")
        child1_happy = SVGMobject("assets/happy.svg")
        child1_group = VGroup(child1_confused, child1_sleepy, child1_excited, child1_skeptical, child1_happy)
        child1_group.scale(.5)
        child1_group.to_edge(LEFT)
        child1_group.to_edge(DOWN)
        child1 = child1_happy
        
        child2_confused = SVGMobject("assets/confused.svg")
        child2_sleepy = SVGMobject("assets/sleepy.svg")
        child2_excited = SVGMobject("assets/excited.svg")
        child2_skeptical = SVGMobject("assets/skeptical.svg")
        child2_happy = SVGMobject("assets/happy.svg")
        child2_group = VGroup(child2_confused, child2_sleepy, child2_excited, child2_skeptical, child2_happy)
        child2_group.scale(.5)
        child2_group.move_to(child1)
        child2_group.shift(RIGHT*1.25)
        child2 = child2_happy
        
        child3_confused = SVGMobject("assets/confused.svg")
        child3_sleepy = SVGMobject("assets/sleepy.svg")
        child3_excited = SVGMobject("assets/excited.svg")
        child3_skeptical = SVGMobject("assets/skeptical.svg")
        child3_happy = SVGMobject("assets/happy.svg")
        child3_group = VGroup(child3_confused, child3_sleepy, child3_excited, child3_skeptical, child3_happy)
        child3_group.scale(.5)
        child3_group.move_to(child2)
        child3_group.shift(RIGHT*1.25)
        child3 = child3_happy
        
        children = VGroup(child1, child2, child3)
        
        socrates = SVGMobject("assets/socrates.svg").scale(.75)
        socrates.to_edge(RIGHT)
        socrates.to_edge(UP)
        
        classroom = VGroup(socrates, children)
        
        self.play(FadeIn(classroom), run_time=2)
        
        # begin adaptation of transcript from http://www.garlikov.com/Soc_Meth.html 
        # reproduced with permission from original author (Rick Garlikov)
        
        ## Today I want to teach you a whole new kind of arithmetic only by asking you questions. I won't be allowed to tell you anything about it, just ask you questions. When you think you know an answer, just yell it out ok?
        
        self.play(Transform(child2,child2_sleepy), run_time=1)
        
        # children ok!
        
        ##############################################################################
        
        # "How many is this?" [I held up ten fingers.]
        socrates_question = Text("How many is this?").scale(.75).move_to(socrates).to_edge(LEFT)
        self.play(FadeIn(socrates_question), run_time=.25)
        
        # TEN
        ten_fingers = SVGMobject("assets/ten_fingers.svg").scale(.75)
        self.play(FadeIn(ten_fingers), run_time=1)
        
        child1_answer = Text("TEN!").scale(.5).move_to(child1).shift(UP*.75)
        child3_answer = Text("TEN!!!").scale(.5).move_to(child3).shift(UP*.75)
        self.play(FadeIn(child1_answer), run_time=.25)
        self.play(FadeIn(child3_answer), run_time=.25)
        self.play(Transform(child2,child2_happy), FadeOut(VGroup(ten_fingers, child1_answer, child3_answer)), run_time=.25)
        
        ##############################################################################
        
        # "Who can write that on the board?"
        socrates_new_question = Text("Who can write that on the board?").scale(.75).move_to(socrates).to_edge(LEFT)
        self.play(Transform(socrates_question,socrates_new_question), run_time=.25)

        # [virtually all hands up; I toss the chalk to one kid and indicate for her to come up and do it]. She writes

        child1_answer = Text("Me!").scale(.5).move_to(child1).shift(UP*.75)
        child2_answer = Text("I can!").scale(.5).move_to(child2).shift(UP*.75)
        child3_answer = Text("Me!").scale(.5).move_to(child3).shift(UP*.75)
        self.play(FadeIn(VGroup(child1_answer, child2_answer, child3_answer)), Transform(child2,child2_excited), run_time=.25)

        board = Rectangle(height=3.75, width=8)
        self.play(Write(board))

        chalk = Text("1 0", font="Eraser")
        self.play(Write(chalk))

        ##############################################################################

        #self.play(Transform(child1,child1_confused), run_time=1)
        #self.play(Transform(child3,child3_sleepy), run_time=1)
        
        # end transcript
