#!/usr/bin/env python3
"""
Question 3 – Recursive turtle pattern (indentation triangle).
"""
import turtle

def draw_segment(t, length, depth):
    if depth == 0:
        t.forward(length); return
    third = length/3
    draw_segment(t, third, depth-1)
    t.left(60);  draw_segment(t, third, depth-1)
    t.right(120);draw_segment(t, third, depth-1)
    t.left(60);  draw_segment(t, third, depth-1)

def draw_polygon_pattern(sides, side_len, depth):
    scr = turtle.Screen(); scr.title("HIT137 Q3 - Recursive Pattern")
    t = turtle.Turtle(); t.speed(0); t.hideturtle()
    angle = 360.0/sides
    t.penup(); t.setpos(-side_len/2, side_len/3); t.pendown()
    for _ in range(sides):
        draw_segment(t, side_len, depth)
        t.right(angle)
    scr.mainloop()

def main():
    try:
        sides = int(input("Enter sides: ").strip())
        side_len = float(input("Enter side length (px): ").strip())
        depth = int(input("Enter recursion depth: ").strip())
    except ValueError:
        print("Invalid input."); return
    if sides < 3 or depth < 0:
        print("Sides >= 3 and depth >= 0."); return
    draw_polygon_pattern(sides, side_len, depth)

if __name__ == "__main__":
    main()
