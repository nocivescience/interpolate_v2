from manim import *
class InterpolateScene2(Scene):
    def construct(self):
        amps=[t for t in np.random.uniform(-3,3,size=14)]
        funcs=self.get_many_func(amps)
        flow_lines=self.get_flow_lines(funcs)
        self.play(Create(funcs))
        self.add(flow_lines)
        self.wait(18)
    def get_many_func(self,amps_var):
        return VGroup(*[
            FunctionGraph(
                lambda t: np.cos(TAU*t)*amp_var,
            )
            for amp_var in amps_var
        ]).set_stroke(width=2,opacity=.2)
    def get_flow_lines(self,func_group):
        window=0.3
        def update_circle(circle,dt):
            circle.total_time+=dt
            diameter=4
            modulus=np.sqrt(diameter)
            alpha=(circle.total_time%modulus)/modulus
            circle.pointwise_become_partial(
                circle.template,
                max(interpolate(-window,1,alpha),0),
                min(interpolate(0,1+window,alpha),1)
            )
        result=VGroup()
        for template in func_group:
            circle=template.copy()
            circle.set_stroke(color=interpolate_color(BLUE_A,BLUE_E,np.random.random()),width=3)
            circle.template=template
            circle.total_time=4*np.random.random()
            circle.add_updater(update_circle)
            result.add(circle)
        return result