from graphe import *;
 

individus = Population()
def max(tab):
    max = tab[0]
    for i in range(0,len(tab)):
        if max < tab[i]:
            max = tab[i]
    return max

def dessine_graphe(tab_infecte):
    n = len(tab_infecte);
    rayon = 2.4;
    move_to(0,LIMITE_SIMULATION_Y+200)
    for i in range(0,n-1):
        set_fill_color(Color.BLACK)
        #fill_circle(i*rayon*2, LIMITE_SIMULATION_Y+200-tab_infecte[i], rayon)
        line_to(i*rayon*2,LIMITE_SIMULATION_Y+200-100*tab_infecte[i]/max(tab_infecte));
def mainloop():
    x = 0
    set_color(Color.BLUE)
    set_fill_color(Color.GREEN)
    tab_infecte = [individus.nombre_infecte]
    temps = 0.0;
    t = 0.0;
    individus.diffuse_vitesse();
    while is_run():
        x = (x + 10) % 440
        if delay_jfps(60):
            infectes_ancien = individus.nombre_infecte;
            clear_device()
            individus.afficher(dt)

            tab_infecte.append(individus.nombre_infecte)
            dessine_graphe(tab_infecte)
            print(t)
            temps = temps+dt;
            print("t = "+str(temps) + " secondes")
            if(temps > 1):
                temps= 0
                individus.diffuse_vitesse();

            #tab_infecte.append(individus.nombre_infecte)
            

def main():
    init_graph(LARGEUR_FENETRE, HAUTEUR_FENETRE)
    set_render_mode(RenderMode.RENDER_MANUAL)
    mainloop()
    close_graph()

easy_run(main)
