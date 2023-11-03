import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class Robot here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Robot extends Actor
{
    public void act() 
    {
        setLocation(getX()-2, getY());
        if (getX() == 0) 
        {
            MyWorld myWorld = (MyWorld)getWorld();
            myWorld.addScore(-30);
            getWorld().removeObject(this);
        }
    }
}
