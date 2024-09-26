import TaskHeading from '../components/TaskHeading/page'
import SubHeading from '../components/SubHeading/page'
import Paragraph from '../components/Paragraph/page'
import Button from '../components/Button/page'
import Link from 'next/link'

const Speaking = () => {
  return (
    <section className='flex flex-col mx-10 items-center justify-center mt-10'>
      <TaskHeading heading='Speaking ability' />
      <SubHeading subHeading='Instruction for Instructor' />
      <ul className="list-disc mt-4">
        <li>Consider all the speech produced by the subject during the test session when rating.</li>
        <li>Do not factor in quantity of speech or word-finding difficulty for this rating.</li>
        <li>Reserve higher scores for subjects whose expressive language is so impaired that they frequently struggle to communicate.</li>
        <li>Focus on how often the subject experiences communication difficulties during the session, not just isolated moments.</li>
      </ul>
      <Link href='/speaking/testspeak'>
      <Button name='Start Test'/>
      </Link>
    </section>
  )
}

export default Speaking
