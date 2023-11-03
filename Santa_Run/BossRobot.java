import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)
public class BossRobot extends Actor
{
    public boolean i = false;
    public void act()
    {
       if (getWorld()!=null)
        {
           i = false;
        }
        else
        {
            i = true;
        }
       if (i = true)
       {   
        if (Greenfoot.getRandomNumber(150) < 1)
        {
           int spawnChance = 3;
           MyWorld myWorld = (MyWorld)getWorld();
           getWorld().addObject(new Bullet(1),800,Greenfoot.getRandomNumber(300));
         }
       }
    }
}
