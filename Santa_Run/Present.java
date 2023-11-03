import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class Present here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Present extends Actor
{
    private int speed;
    public Present()
    {
        speed = Greenfoot.getRandomNumber(2) + 1;
    }
    public void act() 
    {
        setLocation(getX()-speed, getY());
        turn(-1);
        if (getX() == 0) 
        {
            getWorld().removeObject(this);
        }
    }
}
