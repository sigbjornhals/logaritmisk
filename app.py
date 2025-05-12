import numpy as np
import matplotlib.pyplot as plt
import gradio as gr

def plot_exponential(a, b, x_min, x_max, log_x, log_y):
    # 1) Valider grenser
    if x_min >= x_max:
        raise gr.Error("Nedre grense må være mindre enn øvre grense.")
    if log_x and x_min <= 0:
        raise gr.Error("Ved logaritmisk x-akse må nedre grense > 0.")
    
    # 2) Generer data
    x = np.linspace(x_min, x_max, 500)
    y = a * (b ** x)
    
    # 3) Tegn
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(x, y, linewidth=2)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title(r"$f(x)=%.2f\cdot %.2f^x$" % (a, b))
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    
    if log_x:  ax.set_xscale("log")
    if log_y:
        ax.set_yscale("log")
        ax.axhline(1, color="black", linewidth=1)
    else:
        ax.set_ylim(bottom=0)
    
    return fig

# 4) Lag Gradio-interface
demo = gr.Interface(
    fn=plot_exponential,
    inputs=[
        gr.Number(value=2000.0, label="a"),
        gr.Number(value=1.15,  label="b"),
        gr.Number(value=1.0,   label="Nedre x-grense"),
        gr.Number(value=10.0,  label="Øvre x-grense"),
        gr.Checkbox(label="Logaritmisk x-akse", value=False),
        gr.Checkbox(label="Logaritmisk y-akse", value=True),
    ],
    outputs=gr.Plot(label="Graf"),
    title="Logaritmisk skala",
    description="Eksponentialfunksjonen $f(x)=a\\cdot b^x$ med valg av lineær/log-skala."
)

# 5) Kjøre appen
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=8080)
