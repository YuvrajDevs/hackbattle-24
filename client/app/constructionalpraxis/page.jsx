import TaskHeading from '../components/TaskHeading/page'
import SubHeading from '../components/SubHeading/page'
import Paragraph from '../components/Paragraph/page'
import Button from '../components/Button/page'
import Link from 'next/link'

const Page = () => {
    const instruction = 'On the canvas, you will see a shape. Try to draw another one that looks just like it, somewhere on the canvas'
  return (
    <section className='flex flex-col mx-10 items-center justify-center mt-10'>
      <TaskHeading heading='Constructional Praxis'/>
      <SubHeading subHeading='Instructions' />
      <Paragraph para={instruction} />
      <Link href="/constructionalpraxis/drawingtask">
        <Button name='Start Test'/>
      </Link>
    </section>
  )
}

export default Page