from manim import *

class LearningBinary(Scene):
    def construct(self):
        
        intro_1=Text("Can you effectively teach children binary").shift(UP*.5)
        intro_2=Text("arithmetic by only asking questions?").shift(DOWN*.5)
        intro = VGroup(intro_1, intro_2)
        self.add(intro)
        self.wait(3)
        
        reenactment_1 = Text("The following shows a reenacted learning").shift(UP*.5)
        reenactment_2 = Text("session with real third grade children.").shift(DOWN*.5)
        reenactment = VGroup(reenactment_1, reenactment_2)
        self.play(Transform(intro,reenactment))
        self.wait(2)
        
        self.play(FadeOut(intro), run_time=2)
        
        child1_confused = SVGMobject("assets/confused.svg")
        child1_sleepy = SVGMobject("assets/sleepy.svg")
        child1_excited = SVGMobject("assets/excited.svg")
        child1_skeptical = SVGMobject("assets/skeptical.svg")
        child1_happy = SVGMobject("assets/happy.svg")
        child1_neutral = SVGMobject("assets/neutral.svg")
        child1_group = VGroup(child1_confused, child1_sleepy, child1_excited, child1_skeptical, child1_happy, child1_neutral)
        child1_group.scale(.5)
        child1_group.to_edge(LEFT)
        child1_group.to_edge(DOWN)
        child1_group.shift(DOWN*.25)
        child1 = child1_happy
        
        child2_confused = SVGMobject("assets/confused.svg")
        child2_sleepy = SVGMobject("assets/sleepy.svg")
        child2_excited = SVGMobject("assets/excited.svg")
        child2_skeptical = SVGMobject("assets/skeptical.svg")
        child2_happy = SVGMobject("assets/happy.svg")
        child2_neutral = SVGMobject("assets/neutral.svg")
        child2_group = VGroup(child2_confused, child2_sleepy, child2_excited, child2_skeptical, child2_happy, child2_neutral)
        child2_group.scale(.5)
        child2_group.move_to(child1)
        child2_group.shift(RIGHT*1.25)
        child2 = child2_happy
        
        child3_confused = SVGMobject("assets/confused.svg")
        child3_sleepy = SVGMobject("assets/sleepy.svg")
        child3_excited = SVGMobject("assets/excited.svg")
        child3_skeptical = SVGMobject("assets/skeptical.svg")
        child3_happy = SVGMobject("assets/happy.svg")
        child3_neutral = SVGMobject("assets/neutral.svg")
        child3_group = VGroup(child3_confused, child3_sleepy, child3_excited, child3_skeptical, child3_happy, child3_neutral)
        child3_group.scale(.5)
        child3_group.move_to(child2)
        child3_group.shift(RIGHT*1.25)
        child3 = child3_happy
        
        children = VGroup(child1, child2, child3)
        
        socrates = SVGMobject("assets/socrates.svg").scale(.75)
        socrates.to_edge(RIGHT)
        socrates.to_edge(UP)
        socrates.shift(UP*.25)
        
        classroom = VGroup(socrates, children)
        
        self.play(Write(socrates), FadeIn(children), run_time=2)
        
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

        board = Rectangle(height=4, width=8)
        board.shift(UP*.2)
        self.play(Write(board))

        chalk1 = Text("1 0", font="Eraser")
        chalk1.move_to(board)
        chalk1.shift(UP)
        chalk1.shift(LEFT*2)
        self.play(Write(chalk1))
        
        self.play(FadeOut(VGroup(child1_answer, child2_answer, child3_answer)), run_time=.25)
        
        ##############################################################################
        
        # Who can write ten another way? [They hesitate than some hands go up. I toss the chalk to another kid.]
        socrates_new_question = Text("Who can write ten another way?").scale(.75).move_to(socrates).to_edge(LEFT)
        self.play(Transform(socrates_question,socrates_new_question), run_time=.25)
        
        # | | | | | | | | | |
        chalk2 = Text("| | | | | | | | | |", font="Eraser")
        chalk2.move_to(chalk1)
        chalk2.shift(DOWN)
        self.play(Write(chalk2))

        ##############################################################################
        
        # Another way?
        socrates_new_question = Text("Another way?").scale(.75).move_to(socrates).to_edge(LEFT)
        self.play(Transform(socrates_question,socrates_new_question), run_time=.25)
        
        # <s>||||</s> <s>||||</s>
        chalk3 = MarkupText("<s>| | | | </s> <s>| | | | </s>", font="Eraser")
        chalk3.move_to(chalk2)
        chalk3.shift(DOWN)
        self.play(Write(chalk3))
        
        ##############################################################################
        
        # Another way?
        socrates_new_question = Text("Another way again?").scale(.75).move_to(socrates).to_edge(LEFT)
        self.play(Transform(socrates_question,socrates_new_question), run_time=.25)
        
        # 2 x 5 [inspired by the last idea]
        chalk4 = Text("2 x 5", font="Eraser")
        chalk4.move_to(board)
        chalk4.shift(UP)
        chalk4.shift(RIGHT*2)
        self.play(Write(chalk4))
        
        ##############################################################################
        
        # Lots of things that equal ten, right?
        socrates_new_question = Text("Good, but lots of things that equal ten, right?").scale(.75).move_to(socrates).to_edge(LEFT)
        self.play(Transform(socrates_question,socrates_new_question), run_time=.25)
        
        child1_answer = Text("Yes").scale(.5).move_to(child1).shift(UP*.75)
        child2_answer = Text("Yea!").scale(.5).move_to(child2).shift(UP*.75)
        self.play(Transform(child1,child1_happy), Transform(child2,child2_happy), Transform(child3,child3_neutral), FadeIn(VGroup(child1_answer, child2_answer)), run_time=1)
        
        self.play(FadeOut(VGroup(child1_answer, child2_answer)))
        
        ##############################################################################
        
        # Lots of things that equal ten, right?
        socrates_new_question = Text("Can anybody write something else to represent ten?").scale(.75).move_to(socrates).to_edge(LEFT)
        self.play(Transform(socrates_question,socrates_new_question), run_time=.25)
        
        chalk5 = Text("TEN", font="Eraser")
        chalk5.move_to(chalk4)
        chalk5.shift(DOWN)
        self.play(Write(chalk5))
        
        ##############################################################################
        
        # Another way?
        socrates_new_question = Text("Any other ways?").scale(.75).move_to(socrates).to_edge(LEFT)
        self.play(Transform(socrates_question,socrates_new_question), run_time=.25)
        
        chalk6 = Text("X", font="Eraser")
        chalk6.move_to(chalk5)
        chalk6.shift(DOWN)
        self.play(Write(chalk6))
        
        ##############################################################################
        
        # [I point to the word "ten"]. What is this?
        socrates_new_question = Text("What is this?").scale(.75).move_to(socrates).to_edge(LEFT)
        self.play(Transform(socrates_question,socrates_new_question), run_time=.25)
        
        underline_word = Underline(chalk5)
        self.play(Write(underline_word))
        
        self.play(Transform(child3,child3_excited), run_time=.25)
        child1_answer = Text("Ten!").scale(.5).move_to(child1).shift(UP*.75)
        child3_answer = Text("The word ten.").scale(.5).move_to(child3).shift(UP*.75)
        self.play(FadeIn(VGroup(child1_answer, child3_answer)), run_time=.25)
        
        ##############################################################################
        
        # It's a word right?
        socrates_new_question = Text("It's a word right?").scale(.75).move_to(socrates).to_edge(LEFT)
        self.play(Transform(socrates_question,socrates_new_question), run_time=.25)
        
        self.play(FadeOut(VGroup(child1_answer, child3_answer)))
        child1_answer = Text("Yes!").scale(.5).move_to(child1).shift(UP*.75)
        child2_answer = Text("Right!").scale(.5).move_to(child2).shift(UP*.75)
        child3_answer = Text("Yea!").scale(.5).move_to(child3).shift(UP*.75)
        self.play(FadeIn(VGroup(child1_answer, child2_answer, child3_answer)), run_time=.25)
        
        ##############################################################################
        
        # What are written words made up of?
        socrates_new_question = Text("What are written words made up of?").scale(.75).move_to(socrates).to_edge(LEFT)
        self.play(Transform(socrates_question,socrates_new_question), run_time=.25)
        
        ##############################################################################
        
        # How many letters are there in the English alphabet?
        socrates_new_question = Text("How many letters are there in the English alphabet?").scale(.75).move_to(socrates).to_edge(LEFT)
        self.play(Transform(socrates_question,socrates_new_question), run_time=.25)
        
        ##############################################################################
        
        # How many words can you make out of them?
        socrates_new_question = Text("How many words can you make out of them?").scale(.75).move_to(socrates).to_edge(LEFT)
        self.play(Transform(socrates_question,socrates_new_question), run_time=.25)
        
        ##############################################################################

        # [Pointing to the number "10"] What is this way of writing numbers made up of?
        socrates_new_question = Text("What is this way of writing numbers made up of?").scale(.75).move_to(socrates).to_edge(LEFT)
        self.play(Transform(socrates_question,socrates_new_question), run_time=.25)
        
        self.play(FadeOut(underline_word))
        underline_numeral = Underline(chalk1)
        self.play(Write(underline_numeral))
        
        ##############################################################################

        # How many numerals are there?
        socrates_new_question = Text("How many numerals are there?").scale(.75).move_to(socrates).to_edge(LEFT)
        self.play(Transform(socrates_question,socrates_new_question), run_time=.25)
        
        ##############################################################################

        # Which is it, nine or ten?
        socrates_new_question = Text("Which is it, nine or ten?").scale(.75).move_to(socrates).to_edge(LEFT)
        self.play(Transform(socrates_question,socrates_new_question), run_time=.25)
        
        ##############################################################################

        # Starting with zero, what are they? [They call out, I write them in the following way.]
        socrates_new_question = Text("Starting with zero, what are they?").scale(.75).move_to(socrates).to_edge(LEFT)
        self.play(Transform(socrates_question,socrates_new_question), run_time=.25)
        
        self.play(FadeOut(VGroup(chalk1, chalk2, chalk3, chalk4, chalk5, chalk6, underline_numeral)))
        
        number0 = Text("0", font="Eraser").scale(.5).move_to(board).shift(LEFT*3).shift(UP*1.5)
        self.play(Write(number0), run_time=.5)
        number1 = Text("1", font="Eraser").scale(.5).move_to(number0).shift(DOWN*.5)
        self.play(Write(number1), run_time=.5)
        number2 = Text("2", font="Eraser").scale(.5).move_to(number1).shift(DOWN*.5)
        self.play(Write(number2), run_time=.5)
        number3 = Text("3", font="Eraser").scale(.5).move_to(number2).shift(DOWN*.5)
        self.play(Write(number3), run_time=.5)
        number4 = Text("4", font="Eraser").scale(.5).move_to(number3).shift(DOWN*.5)
        self.play(Write(number4), run_time=.5)
        number5 = Text("5", font="Eraser").scale(.5).move_to(number4).shift(DOWN*.5)
        self.play(Write(number5), run_time=.5)
        number6 = Text("6", font="Eraser").scale(.5).move_to(number5).shift(DOWN*.5)
        self.play(Write(number6), run_time=.5)
        number7 = Text("7", font="Eraser").scale(.5).move_to(number0).shift(RIGHT)
        self.play(Write(number7), run_time=.5)
        number8 = Text("8", font="Eraser").scale(.5).move_to(number7).shift(DOWN*.5)
        self.play(Write(number8), run_time=.5)
        number9 = Text("9", font="Eraser").scale(.5).move_to(number8).shift(DOWN*.5)
        self.play(Write(number9), run_time=.5)

        ##############################################################################

        # How many numbers can you make out of these numerals?
        socrates_new_question = Text("How many numbers can you make out of these numerals?").scale(.75).move_to(socrates).to_edge(LEFT)
        self.play(Transform(socrates_question,socrates_new_question), run_time=.25)
        
        ##############################################################################

        # How come we have ten numerals? Could it be because we have 10 fingers?
        socrates_new_question = Text("Why are there ten numerals? Is it because we have 10 fingers?").scale(.75).move_to(socrates).to_edge(LEFT)
        self.play(Transform(socrates_question,socrates_new_question), run_time=.25)
        
        ##############################################################################

        # What if we were aliens with only two fingers? How many numerals might we have?
        socrates_new_question = Text("What if we were aliens with only two fingers? How many numerals might we have?").scale(.75).move_to(socrates).to_edge(LEFT)
        self.play(Transform(socrates_question,socrates_new_question), run_time=.25)

        ##############################################################################

        #self.play(Transform(child1,child1_confused), run_time=1)
        #self.play(Transform(child3,child3_sleepy), run_time=1)
        
        # end transcript
