import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class Bullet here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Bullet extends Actor
{
    /** A bullet looses one life each act, and will disappear when life = 0 */
    private int life = 180;
    public Bullet(int speed)
    {
        super();
    }
    public void act()
    {
        if(life <= 0) {
            getWorld().removeObject(this);
        } 
        else {
            move(-5);
            life--;
            }
        }
}
