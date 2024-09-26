import TaskHeading from '../components/TaskHeading/page'
import SubHeading from '../components/SubHeading/page'
import Paragraph from '../components/Paragraph/page'
import Button from '../components/Button/page'
import Link from 'next/link'

const Page = () => {
    const instruction = 'This task is designed to assess your ability to understand and follow instructions. You will be asked to carry out 5 different commands, with each command having 1 to 5 steps. Please follow the instructions carefully.'
  return (
    <section className='flex flex-col items-center justify-center mt-10'>
      <TaskHeading heading='Commands'/>
      <SubHeading subHeading='Instructions' />
      <Paragraph para={instruction} />
      <Link href="/commands/webcam">
        <Button name='Start Test'/>
      </Link>
    </section>
  )
}

export default Page